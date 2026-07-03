from typing import Iterator

from blockchain.block import Block


class Blockchain:
    """Administra una colección ordenada de `Block`. No valida bloques,
    no calcula hashes, no mina ni persiste."""

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
