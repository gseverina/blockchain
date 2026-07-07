import hashlib
from dataclasses import dataclass

from blockchain.transaction import Transaction


@dataclass(frozen=True)
class Block:
    """Unidad básica de la blockchain: agrupa transacciones, conoce su posición
    y el hash del bloque anterior. Conceptualmente inmutable."""

    transactions: tuple[Transaction, ...]
    index: int
    previous_hash: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "transactions", tuple(self.transactions))
        for tx in self.transactions:
            if not isinstance(tx, Transaction):
                raise TypeError(
                    f"transactions debe contener Transaction, se recibió {type(tx).__name__}"
                )

        if self.index < 0:
            raise ValueError("index no puede ser negativo")

        is_genesis = self.index == 0
        has_previous = self.previous_hash is not None

        if is_genesis and has_previous:
            raise ValueError("el bloque génesis (index=0) no puede tener previous_hash")
        if not is_genesis and not has_previous:
            raise ValueError("todo bloque con index > 0 debe tener previous_hash")

    def hash(self) -> str:
        return hashlib.sha256(repr(self).encode("utf-8")).hexdigest()
