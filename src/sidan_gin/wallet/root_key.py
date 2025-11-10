import CardanoSigner

from sidan_gin.wallet.derivation_indices import DerivationIndices


class RootKeyWallet:
    def __init__(self, root_key: str):
        self.root_key = root_key
        self.derivation_indices = DerivationIndices.default()

    def payment_account(self, account_index: int, key_index: int):
        self.derivation_indices = DerivationIndices.payment(account_index, key_index)

    def stake_account(self, account_index: int, key_index: int):
        self.derivation_indices = DerivationIndices.stake(account_index, key_index)

    def drep_account(self, account_index: int, key_index: int):
        self.derivation_indices = DerivationIndices.drep(account_index, key_index)

    def sign_tx(self, tx_hex: str) -> str:
        return CardanoSigner.sign_bech32(
            self.root_key,
            self.derivation_indices,
            tx_hex,
        )
