import hashlib
from dataclasses import replace

from blockchain.signature import Signature


def public_key_for(private_key: str) -> str:
    return hashlib.sha256(private_key.encode()).hexdigest()


def test_signature_creada_verifica_con_public_key_correcta():
    signature = Signature.create("secreto-alice", "payload")
    assert signature.verify(public_key_for("secreto-alice"), "payload") is True


def test_signature_no_verifica_con_public_key_incorrecta():
    signature = Signature.create("secreto-alice", "payload")
    assert signature.verify(public_key_for("otro-secreto"), "payload") is False


def test_signature_no_verifica_con_payload_distinto():
    signature = Signature.create("secreto-alice", "payload original")
    assert signature.verify(public_key_for("secreto-alice"), "payload modificado") is False


def test_signature_con_content_hash_corrupto_no_verifica():
    signature = Signature.create("secreto-alice", "payload")
    corrupted = replace(signature, content_hash="deadbeef")
    assert corrupted.verify(public_key_for("secreto-alice"), "payload") is False


def test_signature_con_revealed_key_corrupta_no_verifica():
    signature = Signature.create("secreto-alice", "payload")
    corrupted = replace(signature, revealed_key="otro-secreto")
    assert corrupted.verify(public_key_for("secreto-alice"), "payload") is False
