from decimal import Decimal

import pytest

from blockchain.block import Block
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction
from blockchain.wallet import Wallet


def make_transaction(sender="alice", recipient="bob", amount="10"):
    return Transaction(
        sender=Wallet(identifier=sender),
        recipient=Wallet(identifier=recipient),
        amount=Decimal(amount),
    )


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


def test_pending_transactions_vacia_por_defecto():
    chain = Blockchain()
    assert chain.pending_transactions == ()


def test_add_pending_transaction_la_agrega():
    chain = Blockchain()
    tx = make_transaction()
    chain.add_pending_transaction(tx)
    assert chain.pending_transactions == (tx,)


def test_pending_transactions_preserva_orden():
    chain = Blockchain()
    tx1 = make_transaction(amount="1")
    tx2 = make_transaction(amount="2")
    chain.add_pending_transaction(tx1)
    chain.add_pending_transaction(tx2)
    assert chain.pending_transactions == (tx1, tx2)


def test_add_pending_transaction_rechaza_objeto_no_transaction():
    chain = Blockchain()
    with pytest.raises(TypeError):
        chain.add_pending_transaction("no soy una transaction")


def test_add_pending_transaction_no_afecta_los_bloques():
    chain = Blockchain()
    chain.add_pending_transaction(make_transaction())
    assert len(chain) == 0


def test_create_block_en_blockchain_vacia_crea_genesis():
    chain = Blockchain()
    block = chain.create_block()
    assert block.index == 0
    assert block.previous_hash is None
    assert len(chain) == 1


def test_create_block_encadena_correctamente():
    chain = Blockchain()
    genesis = chain.create_block()
    second = chain.create_block()
    assert second.index == 1
    assert second.previous_hash == genesis.hash()


def test_create_block_incluye_transacciones_pendientes():
    chain = Blockchain()
    tx1 = make_transaction(amount="1")
    tx2 = make_transaction(amount="2")
    chain.add_pending_transaction(tx1)
    chain.add_pending_transaction(tx2)
    block = chain.create_block()
    assert block.transactions == (tx1, tx2)


def test_create_block_vacia_las_pendientes():
    chain = Blockchain()
    chain.add_pending_transaction(make_transaction())
    chain.create_block()
    assert chain.pending_transactions == ()


def test_create_block_devuelve_el_bloque_agregado():
    chain = Blockchain()
    block = chain.create_block()
    assert chain[-1] is block


def test_create_block_sin_pendientes_crea_bloque_vacio():
    chain = Blockchain()
    block = chain.create_block()
    assert block.transactions == ()


def test_create_block_sucesivos_mantienen_cadena_valida():
    chain = Blockchain()
    chain.create_block()
    chain.add_pending_transaction(make_transaction())
    chain.create_block()
    chain.add_pending_transaction(make_transaction(amount="2"))
    chain.create_block()
    assert chain.is_valid() is True
