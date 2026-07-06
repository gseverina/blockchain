from dataclasses import FrozenInstanceError

import pytest

from blockchain.wallet import Wallet


def test_crear_wallet():
    wallet = Wallet(identifier="alice")
    assert wallet.identifier == "alice"


def test_wallet_es_inmutable():
    wallet = Wallet(identifier="alice")
    with pytest.raises(FrozenInstanceError):
        wallet.identifier = "bob"


def test_comparacion_por_contenido_iguales():
    a = Wallet(identifier="alice")
    b = Wallet(identifier="alice")
    assert a == b


def test_comparacion_por_contenido_distintas():
    a = Wallet(identifier="alice")
    b = Wallet(identifier="bob")
    assert a != b


def test_identifier_vacio_rechazado():
    with pytest.raises(ValueError):
        Wallet(identifier="")


def test_identifier_solo_espacios_rechazado():
    with pytest.raises(ValueError):
        Wallet(identifier="   ")
