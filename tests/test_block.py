from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from blockchain.block import Block
from blockchain.transaction import Transaction
from blockchain.wallet import Wallet


def make_transaction(sender="alice", recipient="bob", amount="10"):
    return Transaction(
        sender=Wallet(identifier=sender),
        recipient=Wallet(identifier=recipient),
        amount=Decimal(amount),
    )


def test_crear_bloque_genesis():
    block = Block(transactions=(), index=0)
    assert block.index == 0
    assert block.previous_hash is None


def test_crear_bloque_con_previous_hash():
    genesis = Block(transactions=(), index=0)
    block = Block(transactions=(), index=1, previous_hash=genesis.hash())
    assert block.previous_hash == genesis.hash()


def test_bloque_con_cero_transacciones():
    block = Block(transactions=(), index=0)
    assert block.transactions == ()


def test_bloque_almacena_transacciones():
    tx = make_transaction()
    block = Block(transactions=(tx,), index=0)
    assert block.transactions == (tx,)


def test_transactions_se_normaliza_a_tupla():
    tx = make_transaction()
    block = Block(transactions=[tx], index=0)
    assert isinstance(block.transactions, tuple)
    assert block.transactions == (tx,)


def test_transactions_con_elemento_invalido_rechazado():
    with pytest.raises(TypeError):
        Block(transactions=("no es una transaccion",), index=0)


def test_bloque_es_inmutable():
    block = Block(transactions=(), index=0)
    with pytest.raises(FrozenInstanceError):
        block.transactions = (make_transaction(),)


def test_index_negativo_rechazado():
    with pytest.raises(ValueError):
        Block(transactions=(), index=-1)


def test_index_mayor_a_cero_sin_previous_hash_rechazado():
    with pytest.raises(ValueError):
        Block(transactions=(), index=1)


def test_genesis_con_previous_hash_rechazado():
    genesis = Block(transactions=(), index=0)
    with pytest.raises(ValueError):
        Block(transactions=(), index=0, previous_hash=genesis.hash())


def test_hash_es_hex_de_64_caracteres():
    block = Block(transactions=(), index=0)
    h = block.hash()
    assert len(h) == 64
    assert all(c in "0123456789abcdef" for c in h)


def test_hash_mismo_contenido_mismo_hash():
    a = Block(transactions=(), index=0)
    b = Block(transactions=(), index=0)
    assert a.hash() == b.hash()


def test_hash_cambia_si_cambian_las_transacciones():
    a = Block(transactions=(), index=0)
    b = Block(transactions=(make_transaction(),), index=0)
    assert a.hash() != b.hash()


def test_hash_cambia_si_cambia_index():
    genesis = Block(transactions=(), index=0)
    a = Block(transactions=(), index=1, previous_hash=genesis.hash())
    b = Block(transactions=(), index=2, previous_hash=genesis.hash())
    assert a.hash() != b.hash()


def test_hash_cambia_si_cambia_previous_hash():
    genesis_a = Block(transactions=(), index=0)
    genesis_b = Block(transactions=(make_transaction(),), index=0)
    a = Block(transactions=(), index=1, previous_hash=genesis_a.hash())
    b = Block(transactions=(), index=1, previous_hash=genesis_b.hash())
    assert a.hash() != b.hash()


def test_hash_no_modifica_el_bloque():
    block = Block(transactions=(), index=0)
    before = (block.transactions, block.index, block.previous_hash)
    block.hash()
    after = (block.transactions, block.index, block.previous_hash)
    assert before == after
