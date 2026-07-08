from dataclasses import dataclass
from decimal import Decimal

from blockchain.signature import Signature


@dataclass(frozen=True)
class Transaction:
    """Transferencia simple de valor entre dos participantes. Inmutable."""

    sender: str
    recipient: str
    amount: Decimal
    signature: Signature | None = None

    def __post_init__(self) -> None:
        if not self.sender.strip():
            raise ValueError("sender no puede estar vacío")
        if not self.recipient.strip():
            raise ValueError("recipient no puede estar vacío")
        if self.sender == self.recipient:
            raise ValueError("sender y recipient no pueden ser el mismo participante")
        if self.amount <= 0:
            raise ValueError("amount debe ser positivo")
        if self.signature is not None and not isinstance(self.signature, Signature):
            raise TypeError(
                f"signature debe ser Signature o None, se recibió {type(self.signature).__name__}"
            )

    def signing_payload(self) -> str:
        """Representación canónica del contenido firmado — la única fuente
        de verdad compartida entre Wallet.sign() y Transaction.verify()."""
        content = (self.sender, self.recipient, self.amount)
        return repr(content)

    def verify(self, public_key: str) -> bool:
        if self.signature is None:
            return False
        return self.signature.verify(public_key, self.signing_payload())
