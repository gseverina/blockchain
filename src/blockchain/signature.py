import hashlib
from dataclasses import dataclass

# Marcador explícito a nivel de API, no solo en docstrings: este esquema NO
# es criptográficamente seguro y NO debe reutilizarse fuera de este curso.
# `Signature.revealed_key` contiene literalmente la private_key del firmante
# — ver docstring de la clase y "Aclaraciones sobre la implementación" en
# docs/08-digital-signatures.md para la justificación de esta limitación.
INSECURE_EDUCATIONAL_SCHEME = True


@dataclass(frozen=True)
class Signature:
    """Firma digital simplificada, con fines exclusivamente educativos.

    ADVERTENCIA — a diferencia de una firma real (ECDSA/RSA), este esquema
    revela la private_key del firmante dentro de la propia firma
    (`revealed_key`). Es una limitación matemática inevitable: no existe
    forma de que cualquier participante verifique una firma usando
    únicamente una clave pública (un valor hash) sin recurrir a álgebra
    asimétrica real, explícitamente fuera de alcance en este curso. Ver
    "Aclaraciones sobre la implementación" en docs/08-digital-signatures.md.

    No usar este esquema fuera de este curso — ver INSECURE_EDUCATIONAL_SCHEME.
    """

    revealed_key: str
    content_hash: str

    @staticmethod
    def create(private_key: str, payload: str) -> "Signature":
        content_hash = hashlib.sha256((private_key + payload).encode()).hexdigest()
        return Signature(revealed_key=private_key, content_hash=content_hash)

    def verify(self, public_key: str, payload: str) -> bool:
        if hashlib.sha256(self.revealed_key.encode()).hexdigest() != public_key:
            return False
        expected_hash = hashlib.sha256((self.revealed_key + payload).encode()).hexdigest()
        return expected_hash == self.content_hash
