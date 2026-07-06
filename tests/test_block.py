from dataclasses import FrozenInstanceError

import pytest

from blockchain.block import Block


def test_crear_bloque_genesis():
    block = Block(data="genesis", index=0)
    assert block.index == 0
    assert block.previous_hash is None


def test_crear_bloque_con_previous_hash():
    genesis = Block(data="genesis", index=0)
    block = Block(data="segundo", index=1, previous_hash=genesis.hash())
    assert block.previous_hash == genesis.hash()


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


def test_index_mayor_a_cero_sin_previous_hash_rechazado():
    with pytest.raises(ValueError):
        Block(data="x", index=1)


def test_genesis_con_previous_hash_rechazado():
    genesis = Block(data="genesis", index=0)
    with pytest.raises(ValueError):
        Block(data="x", index=0, previous_hash=genesis.hash())


def test_hash_es_hex_de_64_caracteres():
    block = Block(data="genesis", index=0)
    h = block.hash()
    assert len(h) == 64
    assert all(c in "0123456789abcdef" for c in h)


def test_hash_mismo_contenido_mismo_hash():
    a = Block(data="genesis", index=0)
    b = Block(data="genesis", index=0)
    assert a.hash() == b.hash()


def test_hash_cambia_si_cambia_data():
    a = Block(data="genesis", index=0)
    b = Block(data="otro dato", index=0)
    assert a.hash() != b.hash()


def test_hash_cambia_si_cambia_index():
    genesis = Block(data="x", index=0)
    a = Block(data="y", index=1, previous_hash=genesis.hash())
    b = Block(data="y", index=2, previous_hash=genesis.hash())
    assert a.hash() != b.hash()


def test_hash_cambia_si_cambia_previous_hash():
    genesis_a = Block(data="genesis a", index=0)
    genesis_b = Block(data="genesis b", index=0)
    a = Block(data="segundo", index=1, previous_hash=genesis_a.hash())
    b = Block(data="segundo", index=1, previous_hash=genesis_b.hash())
    assert a.hash() != b.hash()


def test_hash_no_modifica_el_bloque():
    block = Block(data="genesis", index=0)
    before = (block.data, block.index, block.previous_hash)
    block.hash()
    after = (block.data, block.index, block.previous_hash)
    assert before == after
