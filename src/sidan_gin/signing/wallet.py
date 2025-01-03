from pycardano import crypto, key
from cbor2 import dumps, loads
from nacl.encoding import RawEncoder
from nacl.hash import blake2b

class HDWallet:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic
        self.hd_wallet = crypto.HDWallet.from_mnemonic(self.mnemonic).derive_from_path("m/1852'/1815'/0'/0/0")
        self.signing_key = key.ExtendedSigningKey.from_hdwallet(self.hd_wallet)
        self.verification_key = self.signing_key.to_verification_key()

    def sign_tx(self, tx_hex):
        raw_decoded_cbor = loads(bytes.fromhex(tx_hex))
        return self.sign(blake2b(dumps(raw_decoded_cbor[0]), 32, encoder=RawEncoder))

    def sign_message_hex(self, message_hex):
        return self.sign(bytes.fromhex(message_hex))

    def sign(self, message):
        return self.signing_key.sign(message).hex()
