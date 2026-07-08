import hashlib
import secrets
from dataclasses import dataclass, field, replace

from blockchain.signature import Signature
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
        # Simplificación educativa: en criptografía real la clave pública se
        # deriva de la privada mediante operaciones sobre curvas elípticas (o
        # equivalentes), no aplicando un hash. Acá usamos sha256(private_key)
        # únicamente para tener una relación unidireccional y determinista sin
        # depender de librerías externas (ver docs/08-digital-signatures.md).
        object.__setattr__(self, "public_key", hashlib.sha256(self.private_key.encode()).hexdigest())

    def sign(self, transaction: Transaction) -> Transaction:
        """Delega el cálculo criptográfico en Signature.create() — Wallet no
        conoce el formato interno de la firma, solo que Signature sabe
        producirla a partir de private_key y un payload."""
        if transaction.sender != self.identifier:
            raise ValueError("solo el emisor puede firmar su propia transacción")
        signature = Signature.create(self.private_key, transaction.signing_payload())
        return replace(transaction, signature=signature)
