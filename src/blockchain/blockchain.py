from typing import Iterator

from blockchain.block import Block


class Blockchain:
    """Administra una colección ordenada de `Block` y verifica la
    integridad del encadenamiento mediante hashes. No mina ni persiste."""

    def __init__(self) -> None:
        self._blocks: list[Block] = []

    def add_block(self, block: Block) -> None:
        """Agrega un bloque existente al final de la cadena.
        En esta versión no se realizan validaciones de consistencia.
        """
        if not isinstance(block, Block):
            raise TypeError(f"se esperaba Block, se recibió {type(block).__name__}")
        self._blocks.append(block)

    def __len__(self) -> int:
        return len(self._blocks)

    def __getitem__(self, index: int) -> Block:
        return self._blocks[index]

    def __iter__(self) -> Iterator[Block]:
        return iter(self._blocks)

    def is_valid(self) -> bool:
        for i in range(1, len(self._blocks)):
            if self._blocks[i].previous_hash != self._blocks[i - 1].hash():
                return False
        return True
