# flake8: noqa: E501

from cbor2 import dumps, loads
from nacl.encoding import RawEncoder
from nacl.hash import blake2b
from pycardano import crypto, key


class HDWallet:
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic
        self.hd_wallet = crypto.HDWallet.from_mnemonic(self.mnemonic).derive_from_path(
            "m/1852'/1815'/0'/0/0"
        )
        self.signing_key = key.ExtendedSigningKey.from_hdwallet(self.hd_wallet)
        self.verification_key = self.signing_key.to_verification_key()

    def sign_tx(self, tx_hex):
        raw_decoded_cbor = loads(bytes.fromhex(tx_hex))
        raw_tx_body = raw_decoded_cbor[0]
        signature = self.sign(blake2b(dumps(raw_tx_body), 32, encoder=RawEncoder))
        raw_witness_set = raw_decoded_cbor[1]
        if 0 in raw_witness_set:
            raw_vkeys = raw_witness_set[0]
            raw_vkeys.append(
                [self.verification_key.to_non_extended().to_cbor()[2::], signature]
            )
            raw_witness_set[0] = raw_vkeys
        else:
            raw_witness_set[0] = [
                [self.verification_key.to_non_extended().to_cbor()[2::], signature]
            ]
        raw_decoded_cbor[1] = raw_witness_set
        return dumps(raw_decoded_cbor).hex()

    def sign_message_hex(self, message_hex):
        return self.sign(bytes.fromhex(message_hex))

    def sign(self, message):
        return self.signing_key.sign(message)
