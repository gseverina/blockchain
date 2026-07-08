import hashlib
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    """Transferencia simple de valor entre dos participantes. Inmutable."""

    sender: str
    recipient: str
    amount: Decimal
    signature: str | None = None

    def __post_init__(self) -> None:
        if not self.sender.strip():
            raise ValueError("sender no puede estar vacío")
        if not self.recipient.strip():
            raise ValueError("recipient no puede estar vacío")
        if self.sender == self.recipient:
            raise ValueError("sender y recipient no pueden ser el mismo participante")
        if self.amount <= 0:
            raise ValueError("amount debe ser positivo")

    def verify(self, public_key: str) -> bool:
        if self.signature is None:
            return False
        content = (self.sender, self.recipient, self.amount)
        expected = hashlib.sha256((public_key + repr(content)).encode()).hexdigest()
        return expected == self.signature
