import unittest
from sidan_gin import HDWallet

class TestWalletSigning(unittest.TestCase):

    def setUp(self):
        self.mnemonic = "summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer summer"
        self.wallet = HDWallet(self.mnemonic)

    def test_sign_message(self):
        tx_hex = "84a500d901028182582038b777a0dbe036b6689346124e5fb928b1d0da40501a93a7f1544a07603659da0101828258390004845038ee499ee8bc0afe56f688f27b2dd76f230d3698a9afcc1b66e0464447c1f51adaefe1ebfb0dd485a349a70479ced1d198cbdf7fe71a1dcd65008258390004845038ee499ee8bc0afe56f688f27b2dd76f230d3698a9afcc1b66e0464447c1f51adaefe1ebfb0dd485a349a70479ced1d198cbdf7fe71a396404dc021a000292dd031a04c67fef0800a0f5f6"
        signature = self.wallet.sign_tx(tx_hex)
        self.assertEqual(signature, "06a0cf0af0402d192c44412ce15d6f428d65a094f2a8f5a74951442004779b6c7d63c6e0bdc90c3925563c5c6081eed5ef92e9d5c8a15802c85b44d9395c3504")

if __name__ == '__main__':
    unittest.main()