import hashlib
import secrets
from dataclasses import dataclass, field, replace

from blockchain.transaction import Transaction


@dataclass(frozen=True)
class Wallet:
    """Representa una identidad dentro de la blockchain, capaz de firmar
    transacciones. Inmutable."""

    identifier: str
    private_key: str = field(default_factory=lambda: secrets.token_hex(32), compare=False, repr=False)
    public_key: str = field(default="", init=False, compare=False)

    def __post_init__(self) -> None:
        if not self.identifier.strip():
            raise ValueError("identifier no puede estar vacío")
        object.__setattr__(self, "public_key", hashlib.sha256(self.private_key.encode()).hexdigest())

    def sign(self, transaction: Transaction) -> Transaction:
        if transaction.sender != self.identifier:
            raise ValueError("solo el emisor puede firmar su propia transacción")
        content = (transaction.sender, transaction.recipient, transaction.amount)
        signature = hashlib.sha256((self.public_key + repr(content)).encode()).hexdigest()
        return replace(transaction, signature=signature)
