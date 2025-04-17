from typing import Union

from ..python_signing_module import CardanoSigner
from .derivation_indices import DerivationIndices


class MnemonicWallet:
    def __init__(self, mnemonic_phrase: str):
        self.mnemonic_phrase = mnemonic_phrase
        self.derivation_indices = DerivationIndices.default()

    def payment_account(self, account_index: int, key_index: int):
        self.derivation_indices = DerivationIndices.payment(account_index, key_index)

    def stake_account(self, account_index: int, key_index: int):
        self.derivation_indices = DerivationIndices.stake(account_index, key_index)

    def drep_account(self, account_index: int, key_index: int):
        self.derivation_indices = DerivationIndices.drep(account_index, key_index)

    def sign_tx(self, tx_hex: str) -> str:
        return CardanoSigner.sign_mnemonic(
            self.mnemonic_phrase,
            self.derivation_indices,
            tx_hex,
        )


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
        # Implement according to your CardanoSigner capabilities
        return CardanoSigner.sign_root_key(
            self.root_key,
            self.derivation_indices,
            tx_hex,
        )


class CliWallet:
    def __init__(self, cli_skey: str):
        self.cli_skey = cli_skey

    def sign_tx(self, tx_hex: str) -> str:
        # Implement CLI-based signing
        return CardanoSigner.sign_cli_key(
            self.cli_skey,
            tx_hex,
        )


# Main Wallet class that users will interact with
class Wallet:
    def __init__(self, wallet_type: Union[MnemonicWallet, RootKeyWallet, CliWallet]):
        self.wallet_type = wallet_type

    @classmethod
    def new_mnemonic(cls, mnemonic_phrase: str) -> "Wallet":
        """Create a new wallet from a mnemonic phrase"""
        return cls(MnemonicWallet(mnemonic_phrase))

    @classmethod
    def new_root_key(cls, root_key: str) -> "Wallet":
        """Create a new wallet from a root key"""
        return cls(RootKeyWallet(root_key))

    @classmethod
    def new_cli(cls, cli_skey: str) -> "Wallet":
        """Create a new wallet that uses CLI signing"""
        return cls(CliWallet(cli_skey))

    def payment_account(self, account_index: int, key_index: int) -> "Wallet":
        """Configure for payment account operations"""
        if isinstance(self.wallet_type, (MnemonicWallet, RootKeyWallet)):
            self.wallet_type.payment_account(account_index, key_index)
        return self

    def stake_account(self, account_index: int, key_index: int) -> "Wallet":
        """Configure for stake account operations"""
        if isinstance(self.wallet_type, (MnemonicWallet, RootKeyWallet)):
            self.wallet_type.stake_account(account_index, key_index)
        return self

    def drep_account(self, account_index: int, key_index: int) -> "Wallet":
        """Configure for drep account operations"""
        if isinstance(self.wallet_type, (MnemonicWallet, RootKeyWallet)):
            self.wallet_type.drep_account(account_index, key_index)
        return self

    def sign_tx(self, tx_hex: str) -> str:
        """Sign a transaction using the configured wallet"""
        return self.wallet_type.sign_tx(tx_hex)
