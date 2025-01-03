import unittest
from sidan_gin import HDWallet

class TestWalletSigning(unittest.TestCase):

    def setUp(self):
        self.mnemonic = "summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer"
        self.wallet = HDWallet(self.mnemonic)

    def test_sign_message(self):
        tx_hex = "828bba9771a87dd61fe0b7136946eb897c27cfc15e71e249cbfaab5c03929fb6"
        signature = self.wallet.sign_tx(tx_hex)
        self.assertEqual(signature, "06a0cf0af0402d192c44412ce15d6f428d65a094f2a8f5a74951442004779b6c7d63c6e0bdc90c3925563c5c6081eed5ef92e9d5c8a15802c85b44d9395c3504")

if __name__ == '__main__':
    unittest.main()