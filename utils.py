from base64 import urlsafe_b64encode
from hashlib import sha256
from uuid import uuid4

from cryptography.fernet import Fernet

from entity import GenerateRequest
from storage.db import DataBaseInterface


def generate_key(input_string) -> bytes:
    return urlsafe_b64encode(sha256(input_string.encode("utf-8")).digest()[:32])


def encrypt_string(text, key) -> bytes:
    return Fernet(key).encrypt(text.encode("utf-8"))


def decrypt_string(cipher_text, key) -> str:
    return Fernet(key).decrypt(cipher_text).decode("utf-8")
