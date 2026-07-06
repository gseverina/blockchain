from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    """Transferencia simple de valor entre dos participantes. Inmutable."""

    sender: str
    recipient: str
    amount: Decimal

    def __post_init__(self) -> None:
        if not self.sender.strip():
            raise ValueError("sender no puede estar vacío")
        if not self.recipient.strip():
            raise ValueError("recipient no puede estar vacío")
        if self.sender == self.recipient:
            raise ValueError("sender y recipient no pueden ser el mismo participante")
        if self.amount <= 0:
            raise ValueError("amount debe ser positivo")
