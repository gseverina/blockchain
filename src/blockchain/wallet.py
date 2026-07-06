from dataclasses import dataclass


@dataclass(frozen=True)
class Wallet:
    """Representa una identidad dentro de la blockchain. Inmutable."""

    identifier: str

    def __post_init__(self) -> None:
        if not self.identifier.strip():
            raise ValueError("identifier no puede estar vacío")
