import unittest

from sidan_gin import decrypt_with_cipher, encrypt_with_cipher


class TestCipher(unittest.TestCase):
    def test_decrypt_with_cipher(self):
        data = "solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution"
        key = "01234567890123456789"

        encrypted_data = {
            "iv": "/bs1AzciZ1bDqT5W",
            "ciphertext": "mh5pgH8ErqqH2KLLEBqqr8Pwm+mUuh9HhaAHslSD8ho6zk7mXccc9NUQAW8rb9UajCq8LYyANuiorjYD5N0hd2Lbe2n1x8AGRZrogyRKW6uhoFD1/FW6ofjgGP/kQRQSW2ZdJaDMbCxwYSdzxmaRunk6JRfybhfRU6kIxPMu41jhhRC3LbwZ+NnfBJFrg859hbuQgMQm8mqOUgOxcK8kKH54shOpGuLT4YBXhx33dZ//wT5VXrQ8kwIKttNk5h9MNKCacpRZSqU3pGlZ5oxucNEGos0IKTTXfbmwYx14uiERcXd32OP2",
        }
        encrypted_data_str = '{"iv":"%s","ciphertext":"%s"}' % (
            encrypted_data["iv"],
            encrypted_data["ciphertext"],
        )

        decrypted_data = decrypt_with_cipher(encrypted_data_str, key)
        self.assertEqual(data, decrypted_data)

    def test_encrypt_and_decrypt_with_cipher(self):
        data = "solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution solution"
        key = "01234567890123456789"

        encrypted_data = encrypt_with_cipher(data, key, 12)
        decrypted_data = decrypt_with_cipher(encrypted_data, key)

        self.assertEqual(data, decrypted_data)


if __name__ == "__main__":
    unittest.main()
