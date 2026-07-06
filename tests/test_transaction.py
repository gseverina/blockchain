from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from blockchain.transaction import Transaction


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
