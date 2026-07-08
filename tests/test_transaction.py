from dataclasses import FrozenInstanceError, replace
from decimal import Decimal

import pytest

from blockchain.transaction import Transaction
from blockchain.wallet import Wallet


def test_crear_transaccion_valida():
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10.50"))
    assert tx.sender == "alice"
    assert tx.recipient == "bob"
    assert tx.amount == Decimal("10.50")


def test_transaccion_es_inmutable():
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    with pytest.raises(FrozenInstanceError):
        tx.amount = Decimal("20")


def test_comparacion_por_contenido_iguales():
    a = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    b = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    assert a == b


def test_comparacion_por_contenido_distinto_amount():
    a = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    b = Transaction(sender="alice", recipient="bob", amount=Decimal("20"))
    assert a != b


def test_amount_cero_rechazado():
    with pytest.raises(ValueError):
        Transaction(sender="alice", recipient="bob", amount=Decimal("0"))


def test_amount_negativo_rechazado():
    with pytest.raises(ValueError):
        Transaction(sender="alice", recipient="bob", amount=Decimal("-5"))


def test_sender_vacio_rechazado():
    with pytest.raises(ValueError):
        Transaction(sender="   ", recipient="bob", amount=Decimal("10"))


def test_recipient_vacio_rechazado():
    with pytest.raises(ValueError):
        Transaction(sender="alice", recipient="", amount=Decimal("10"))


def test_sender_igual_a_recipient_rechazado():
    with pytest.raises(ValueError):
        Transaction(sender="alice", recipient="alice", amount=Decimal("10"))


def test_transaccion_sin_firmar_no_verifica():
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    alice = Wallet(identifier="alice")
    assert tx.verify(alice.public_key) is False


def test_transaccion_firmada_verifica_con_public_key_correcta():
    alice = Wallet(identifier="alice")
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    signed = alice.sign(tx)
    assert signed.verify(alice.public_key) is True


def test_transaccion_firmada_no_verifica_con_otra_public_key():
    alice = Wallet(identifier="alice")
    otra = Wallet(identifier="mallory")
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    signed = alice.sign(tx)
    assert signed.verify(otra.public_key) is False


def test_transaccion_modificada_deja_de_verificar():
    alice = Wallet(identifier="alice")
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    signed = alice.sign(tx)
    tampered = replace(signed, amount=Decimal("999"))
    assert tampered.verify(alice.public_key) is False


def test_firma_invalida_no_verifica():
    alice = Wallet(identifier="alice")
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    signed = alice.sign(tx)
    corrupted = replace(signed, signature=replace(signed.signature, content_hash="deadbeef"))
    assert corrupted.verify(alice.public_key) is False


def test_signature_de_tipo_invalido_rechazada():
    with pytest.raises(TypeError):
        Transaction(sender="alice", recipient="bob", amount=Decimal("10"), signature="no es un Signature")


def test_verify_no_modifica_la_transaccion():
    alice = Wallet(identifier="alice")
    tx = Transaction(sender="alice", recipient="bob", amount=Decimal("10"))
    signed = alice.sign(tx)
    before = (signed.sender, signed.recipient, signed.amount, signed.signature)
    signed.verify(alice.public_key)
    after = (signed.sender, signed.recipient, signed.amount, signed.signature)
    assert before == after
