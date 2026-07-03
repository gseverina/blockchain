from dataclasses import FrozenInstanceError

import pytest

from blockchain.block import Block


def test_crear_bloque_genesis():
    block = Block(data="genesis", index=0)
    assert block.index == 0
    assert block.previous_block is None


def test_crear_bloque_con_previous():
    genesis = Block(data="genesis", index=0)
    block = Block(data="segundo", index=1, previous_block=genesis)
    assert block.previous_block is genesis


def test_acceso_a_atributos():
    block = Block(data={"a": 1}, index=0)
    assert block.data == {"a": 1}
    assert block.index == 0


def test_bloque_es_inmutable():
    block = Block(data="genesis", index=0)
    with pytest.raises(FrozenInstanceError):
        block.data = "otro"


def test_index_negativo_rechazado():
    with pytest.raises(ValueError):
        Block(data="x", index=-1)


def test_index_mayor_a_cero_sin_previous_rechazado():
    with pytest.raises(ValueError):
        Block(data="x", index=1)


def test_genesis_con_previous_rechazado():
    genesis = Block(data="genesis", index=0)
    with pytest.raises(ValueError):
        Block(data="x", index=0, previous_block=genesis)
