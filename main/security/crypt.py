import base64
import os

from Crypto.Cipher import AES


class AesCipherHandler:
    """
    Class which stores an encrypted message in a certain format
    and provides methods for encryption and decryption using the AES algorithm
    """

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
        """
        Check if encryption is set, otherwise a value error is thrown
        """
        if None in [self._tag, self._cipher_text, self._nonce]:
            raise ValueError("no encryption is made")

    def __init__(self):
        self._tag = None
        self._nonce = None
        self._cipher_text = None

    def set_encryption(self, key: str, message: str):
        """
        Encrypts the message using a key and stores the encryption into the class
        """
        bytes_key = bytes(key, self._byte_encoding)
        bytes_message = bytes(message, self._byte_encoding)

        cipher = AES.new(bytes_key, AES.MODE_EAX)

        self._nonce = cipher.nonce
        self._cipher_text, self._tag = cipher.encrypt_and_digest(bytes_message)

    def set_encrypted_message(self, encrypted: str):
        """
        Stores an encrypted message utilizing this class's formatting system.
        To be used for encrypted messages already encrypted by this class
        """
        encrypted_bytes = base64.b64decode(encrypted.encode(self._byte_encoding))
        self._tag = encrypted_bytes[:self._tag_size]
        self._cipher_text = encrypted_bytes[self._tag_size:-self._nonce_size]
        self._nonce = encrypted_bytes[-self._nonce_size:]

    def decrypt(self, key: str) -> str:
        """
        Decrypts a stored message provided the encryption is set.
        Otherwise a value error is thrown
        """
        self._assert_encrypted()
        bytes_key = bytes(key, self._byte_encoding)
        cipher = AES.new(bytes_key, AES.MODE_EAX, nonce=self._nonce)
        plaintext = cipher.decrypt(self._cipher_text)
        cipher.verify(self._tag)
        return plaintext.decode(self._byte_encoding)

    @property
    def encrypted_message(self) -> str:
        """
        Returns an encrypted message assuming an encryption is set.
        Otherwise a value error is thrown
        """
        self._assert_encrypted()
        bytes_message = self._tag + self._cipher_text + self._nonce
        return base64.b64encode(bytes_message).decode(self._byte_encoding)


def get_aes_key():
    return os.environ.get("AES_KEY")


def aes_encrypt(message: str) -> str:
    """
    encrypts message using the AES algorithm, throws a value error
    """
    key = get_aes_key()
    cipher_handler = AesCipherHandler()
    cipher_handler.set_encryption(key, message)
    return cipher_handler.encrypted_message


def aes_decrypt(encrypted: str):
    """
    decrypts an encrypted message using the AES algorithm, throws a value error
    """
    key = get_aes_key()
    cipher_handler = AesCipherHandler()
    cipher_handler.set_encrypted_message(encrypted)
    return cipher_handler.decrypt(key)
