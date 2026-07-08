from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from blockchain.transaction import Transaction
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


def test_wallet_genera_keys_automaticamente():
    wallet = Wallet(identifier="alice")
    assert wallet.private_key
    assert wallet.public_key


def test_dos_wallets_tienen_keys_distintas():
    a = Wallet(identifier="alice")
    b = Wallet(identifier="bob")
    assert a.private_key != b.private_key
    assert a.public_key != b.public_key


def test_public_key_es_hash_de_private_key():
    import hashlib

    wallet = Wallet(identifier="alice")
    assert wallet.public_key == hashlib.sha256(wallet.private_key.encode()).hexdigest()


def test_sign_devuelve_nueva_transaccion_firmada():
    alice = Wallet(identifier="alice")
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    signed = alice.sign(tx)
    assert signed is not tx
    assert signed.signature is not None
    assert tx.signature is None


def test_sign_rechaza_transaccion_de_otro_sender():
    alice = Wallet(identifier="alice")
    tx = Transaction(sender="bob", recipient="carol", amount=Decimal("10"))
    with pytest.raises(ValueError):
        alice.sign(tx)
