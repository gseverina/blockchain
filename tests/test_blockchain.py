import pytest

from blockchain.block import Block
from blockchain.blockchain import Blockchain


def test_blockchain_vacia():
    chain = Blockchain()
    assert len(chain) == 0


def test_add_block_incrementa_len():
    chain = Blockchain()
    chain.add_block(Block(data="genesis", index=0))
    assert len(chain) == 1


def test_preserva_orden_de_insercion():
    chain = Blockchain()
    genesis = Block(data="genesis", index=0)
    second = Block(data="segundo", index=1, previous_hash=genesis.hash())
    chain.add_block(genesis)
    chain.add_block(second)
    assert chain[0] is genesis
    assert chain[1] is second


def test_iterar_recorre_todos_en_orden():
    chain = Blockchain()
    genesis = Block(data="genesis", index=0)
    second = Block(data="segundo", index=1, previous_hash=genesis.hash())
    chain.add_block(genesis)
    chain.add_block(second)
    assert list(chain) == [genesis, second]


def test_add_block_rechaza_objeto_no_block():
    chain = Blockchain()
    with pytest.raises(TypeError):
        chain.add_block("no soy un block")


def test_acceso_fuera_de_rango_levanta_index_error():
    chain = Blockchain()
    with pytest.raises(IndexError):
        chain[0]
