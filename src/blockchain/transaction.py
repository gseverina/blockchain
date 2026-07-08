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

    def signing_payload(self) -> str:
        """Representación estable del contenido a firmar/verificar.
        Única fuente de verdad compartida entre Wallet.sign() y verify()."""
        content = (self.sender, self.recipient, self.amount)
        return repr(content)

    def verify(self, public_key: str) -> bool:
        """Simplificación educativa: la firma revela la private_key usada
        para producirla. Se verifica que esa clave revelada corresponda al
        `public_key` publicado (commitment sha256) y que efectivamente haya
        producido el hash de contenido almacenado en la firma. No es segura
        para reutilización de clave (ver docs/08-digital-signatures.md)."""
        if self.signature is None:
            return False
        try:
            revealed_key, content_hash = self.signature.split(":", 1)
        except ValueError:
            return False
        if hashlib.sha256(revealed_key.encode()).hexdigest() != public_key:
            return False
        expected_hash = hashlib.sha256((revealed_key + self.signing_payload()).encode()).hexdigest()
        return expected_hash == content_hash
