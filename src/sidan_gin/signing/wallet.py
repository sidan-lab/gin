from pycardano import crypto, key, transaction

class HDWallet:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic
        self.hd_wallet = crypto.HDWallet.from_mnemonic(self.mnemonic).derive_from_path("m/1852'/1815'/0'/0/0")
        self.signing_key = key.ExtendedSigningKey.from_hdwallet(self.hd_wallet)
        self.verification_key = self.signing_key.to_verification_key()

    def sign_tx(self, tx_hex):
        tx = transaction.Transaction.from_cbor(tx_hex)
        return self.sign(tx.transaction_body.id)

    def sign_message_hex(self, message_hex):
        return self.sign(bytes.fromhex(message_hex))

    def sign(self, message):
        return self.signing_key.sign(message).hex()
