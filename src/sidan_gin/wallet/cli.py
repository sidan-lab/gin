import CardanoSigner


class CliWallet:
    def __init__(self, cli_skey: str):
        self.cli_skey = cli_skey

    def sign_tx(self, tx_hex: str) -> str:
        # Implement CLI-based signing
        return CardanoSigner.sign_cli(
            self.cli_skey,
            tx_hex,
        )
