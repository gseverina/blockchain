from typing import Iterator

from blockchain.block import Block
from blockchain.transaction import Transaction


class Blockchain:
    """Administra una colección ordenada de `Block` y las transacciones
    pendientes de incorporarse a un bloque. Verifica la integridad del
    encadenamiento mediante hashes. No mina ni persiste."""

    def __init__(self) -> None:
        self._blocks: list[Block] = []
        self._pending_transactions: list[Transaction] = []

    def add_block(self, block: Block) -> None:
        """Agrega un bloque existente al final de la cadena.
        En esta versión no se realizan validaciones de consistencia.
        """
        if not isinstance(block, Block):
            raise TypeError(f"se esperaba Block, se recibió {type(block).__name__}")
        self._blocks.append(block)

    def add_pending_transaction(self, transaction: Transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise TypeError(
                f"se esperaba Transaction, se recibió {type(transaction).__name__}"
            )
        self._pending_transactions.append(transaction)

    @property
    def pending_transactions(self) -> tuple[Transaction, ...]:
        return tuple(self._pending_transactions)

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
