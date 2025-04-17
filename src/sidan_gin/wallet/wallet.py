from ..python_signing_module import CardanoSigner

class HDWallet:
    def __init__(self, mnemonic, account_index=0, key_index=0):
        self.mnemonic = mnemonic
        self.account_index = account_index
        self.key_index = key_index

    def sign_tx(self, tx_hex):
        return CardanoSigner.sign_mnemonic(
            self.mnemonic,
            self.account_index,
            self.key_index,
            tx_hex
        )
