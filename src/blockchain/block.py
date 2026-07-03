import hashlib
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Block:
    """Unidad básica de la blockchain: almacena datos, conoce su posición
    y mantiene una referencia al bloque anterior. Conceptualmente inmutable."""

    data: Any
    index: int
    previous_block: "Block | None" = None

    def __post_init__(self) -> None:
        if self.index < 0:
            raise ValueError("index no puede ser negativo")

        is_genesis = self.index == 0
        has_previous = self.previous_block is not None

        if is_genesis and has_previous:
            raise ValueError("el bloque génesis (index=0) no puede tener previous_block")
        if not is_genesis and not has_previous:
            raise ValueError("todo bloque con index > 0 debe tener previous_block")

    def hash(self) -> str:
        return hashlib.sha256(repr(self).encode("utf-8")).hexdigest()
