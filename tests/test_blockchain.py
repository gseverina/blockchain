import pytest

from blockchain.block import Block
from blockchain.blockchain import Blockchain


def test_blockchain_vacia():
    chain = Blockchain()
    assert len(chain) == 0


def test_add_block_incrementa_len():
    chain = Blockchain()
    chain.add_block(Block(transactions=(), index=0))
    assert len(chain) == 1


def test_preserva_orden_de_insercion():
    chain = Blockchain()
    genesis = Block(transactions=(), index=0)
    second = Block(transactions=(), index=1, previous_hash=genesis.hash())
    chain.add_block(genesis)
    chain.add_block(second)
    assert chain[0] is genesis
    assert chain[1] is second


def test_iterar_recorre_todos_en_orden():
    chain = Blockchain()
    genesis = Block(transactions=(), index=0)
    second = Block(transactions=(), index=1, previous_hash=genesis.hash())
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


def test_blockchain_vacia_es_valida():
    chain = Blockchain()
    assert chain.is_valid() is True


def test_blockchain_solo_genesis_es_valida():
    chain = Blockchain()
    chain.add_block(Block(transactions=(), index=0))
    assert chain.is_valid() is True


def test_blockchain_bien_encadenada_es_valida():
    chain = Blockchain()
    genesis = Block(transactions=(), index=0)
    chain.add_block(genesis)
    previous = genesis
    for i in range(1, 4):
        block = Block(transactions=(), index=i, previous_hash=previous.hash())
        chain.add_block(block)
        previous = block
    assert chain.is_valid() is True


def test_blockchain_con_previous_hash_incorrecto_es_invalida():
    chain = Blockchain()
    genesis = Block(transactions=(), index=0)
    chain.add_block(genesis)
    chain.add_block(Block(transactions=(), index=1, previous_hash=genesis.hash()))
    chain.add_block(Block(transactions=(), index=2, previous_hash="hash inventado"))
    assert chain.is_valid() is False


def test_is_valid_no_modifica_la_blockchain():
    chain = Blockchain()
    genesis = Block(transactions=(), index=0)
    chain.add_block(genesis)
    chain.add_block(Block(transactions=(), index=1, previous_hash=genesis.hash()))
    before = list(chain)
    chain.is_valid()
    after = list(chain)
    assert before == after
