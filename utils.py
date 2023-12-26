from base64 import urlsafe_b64encode
from hashlib import sha256

from cryptography.fernet import Fernet


def generate_key(input_string) -> bytes:
    """
    Generate encode key for input string.
    :param input_string: salt or password
    :return: encoded bytes
    """
    return urlsafe_b64encode(sha256(input_string.encode("utf-8")).digest()[:32])


def encrypt_string(text, key) -> bytes:
    """
    Encrypt text.
    :param text: what you want to encrypt
    :param key: key for encryption
    :return: encrypted text
    """
    return Fernet(key).encrypt(text.encode("utf-8"))


def decrypt_string(cipher_text, key) -> str:
    """
    Decrypt text.
    :param cipher_text: encrypted text
    :param key: key for decryption (password or salt)
    :return: original text
    """
    return Fernet(key).decrypt(cipher_text).decode("utf-8")
