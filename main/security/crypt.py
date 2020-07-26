import os

from Crypto.Cipher import AES
import base64


class AesCipherHandler:

    @property
    def _byte_encoding(self):
        return 'utf-8'

    @property
    def _tag_size(self):
        return 16

    @property
    def _nonce_size(self):
        return 16

    def _assert_encrypted(self):
        if None in [self._tag, self._cipher_text, self._nonce]:
            raise ValueError("no encryption is made")

    def __init__(self):
        self._tag = None
        self._nonce = None
        self._cipher_text = None

    def set_encryption(self, key: str, message: str):
        byte_key = bytes(key, self._byte_encoding)
        byte_message = bytes(message, self._byte_encoding)

        cipher = AES.new(byte_key, AES.MODE_EAX)

        self._nonce = cipher.nonce
        self._cipher_text, self._tag = cipher.encrypt_and_digest(byte_message)

    def set_encrypted_message(self, encrypted: str):
        encrypted_bytes = base64.b64decode(encrypted.encode(self._byte_encoding))
        self._tag = encrypted_bytes[:self._tag_size]
        self._cipher_text = encrypted_bytes[self._tag_size:-self._nonce_size]
        self._nonce = encrypted_bytes[-self._nonce_size:]

    def decrypt(self, key: str) -> str:
        self._assert_encrypted()
        byte_key = bytes(key, self._byte_encoding)
        cipher = AES.new(byte_key, AES.MODE_EAX, nonce=self._nonce)
        plaintext = cipher.decrypt(self._cipher_text)
        cipher.verify(self._tag)
        return plaintext.decode(self._byte_encoding)

    @property
    def encrypted_message(self) -> str:
        self._assert_encrypted()
        bytes_message = self._tag + self._cipher_text + self._nonce
        return base64.b64encode(bytes_message).decode(self._byte_encoding)


def get_aes_key():
    return os.environ.get("AES_KEY")


def aes_encrypt(message: str) -> str:
    key = get_aes_key()
    cipher_handler = AesCipherHandler()
    cipher_handler.set_encryption(key, message)
    return cipher_handler.encrypted_message


def aes_decrypt(encrypted: str):
    key = get_aes_key()
    cipher_handler = AesCipherHandler()
    cipher_handler.set_encrypted_message(encrypted)
    return cipher_handler.decrypt(key)
