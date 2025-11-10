import base64
import json
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt_with_cipher(
    data: str, key: str, initialization_vector_size: int = 12
) -> str:
    """
    Encrypt data using AES-GCM with a derived key from PBKDF2 and SHA-256.

    :param data: The plaintext data to encrypt.
    :param key: The input key used for encryption.
    :param initialization_vector_size: The size of the IV (default is 12 bytes for AES-GCM).
    :return: A JSON string containing the IV and ciphertext (both base64-encoded).
    :raises ValueError: If encryption fails or input data is invalid.
    """
    # Derive a cryptographic key from the input key using PBKDF2 and SHA-256
    salt = bytes(
        initialization_vector_size
    )  # Using a fixed salt (empty for simplicity)
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,  # AES-256 requires a 256-bit key (32 bytes)
        salt=salt,
        iterations=100_000,
        backend=default_backend(),
    )
    derived_key = kdf.derive(key.encode())

    # Generate a random IV
    iv = os.urandom(initialization_vector_size)  # Generate a random IV
    try:
        # Initialize AES-GCM cipher
        cipher = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(iv),
            backend=default_backend(),
        )
        encryptor = cipher.encryptor()

        # Encrypt the data
        ciphertext = encryptor.update(data.encode()) + encryptor.finalize()

        # Get the authentication tag
        tag = encryptor.tag

        # Append the tag to the ciphertext to match Web Crypto API behavior
        ciphertext_with_tag = ciphertext + tag
    except Exception as e:
        raise ValueError("Encryption failed") from e

    # Encode the IV and ciphertext (with tag) in base64
    iv_base64 = base64.b64encode(iv).decode("utf-8")
    ciphertext_base64 = base64.b64encode(ciphertext_with_tag).decode("utf-8")

    # Create a JSON-like string containing the IV and ciphertext
    result = {
        "iv": iv_base64,
        "ciphertext": ciphertext_base64,
    }

    return json.dumps(result)


def decrypt_with_cipher(encrypted_data_json: str, key: str) -> str:
    """
    Decrypt data encrypted with AES-GCM using a derived key from PBKDF2 and SHA-256.
    Supports both new format (with salt) and legacy format (without salt) for backward compatibility.
    """
    # Parse the encrypted data from JSON
    try:
        encrypted_data = json.loads(encrypted_data_json)
        iv_base64 = encrypted_data["iv"]
        ciphertext_base64 = encrypted_data["ciphertext"]
        salt_base64 = encrypted_data.get("salt")  # Optional for backward compatibility
    except (KeyError, json.JSONDecodeError) as e:
        raise ValueError("Invalid encrypted data JSON") from e

    # Decode IV from base64
    try:
        iv = base64.b64decode(iv_base64)
    except base64.binascii.Error as e:
        raise ValueError("Failed to decode IV") from e

    # Decode ciphertext from base64
    try:
        ciphertext_with_tag = base64.b64decode(ciphertext_base64)
    except base64.binascii.Error as e:
        raise ValueError("Failed to decode ciphertext") from e

    # Handle salt - support both new format (with salt) and legacy format (without salt)
    if salt_base64 is not None and salt_base64 != "":
        # New format: use the provided salt
        try:
            salt = base64.b64decode(salt_base64)
        except base64.binascii.Error as e:
            raise ValueError("Failed to decode salt") from e
    else:
        # Legacy format: use zero-filled salt of IV length for backward compatibility
        salt = bytes(len(iv))

    # Derive cryptographic key from password using PBKDF2
    # Matches frontend: 100,000 iterations, SHA-256, 256-bit key
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,  # AES-256 requires a 256-bit key (32 bytes)
        salt=salt,
        iterations=100_000,
        backend=default_backend(),
    )
    derived_key = kdf.derive(key.encode())

    # In GCM mode, the tag is appended to the ciphertext
    # Standard GCM tag length is 16 bytes (128 bits)
    tag_length = 16
    ciphertext = ciphertext_with_tag[:-tag_length]
    tag = ciphertext_with_tag[-tag_length:]

    # Initialize AES-GCM cipher for decryption
    try:
        cipher = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(iv, tag),  # Pass the extracted tag to GCM mode
            backend=default_backend(),
        )
        decryptor = cipher.decryptor()

        # Decrypt the data
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    except Exception as e:
        raise ValueError(
            "Failed to decrypt (incorrect password or corrupted data)"
        ) from e

    # Convert the decrypted data back to a string
    try:
        decrypted_str = decrypted_data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise ValueError("Failed to convert decrypted data to UTF-8") from e

    return decrypted_str
