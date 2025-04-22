class DerivationIndices:
    @classmethod
    def default(cls):
        """Default derivation indices (payment with index 0)"""
        return DerivationIndices.payment(0, 0)

    @classmethod
    def payment(cls, account_index: int, key_index: int):
        """Creates derivation indices for payment accounts"""
        return DerivationIndices.raw_path(
            ["1852'", "1815'", f"{str(account_index)}'", str(0), str(key_index)]
        )

    @classmethod
    def stake(cls, account_index: int, key_index: int):
        """Creates derivation indices for stake accounts"""
        return DerivationIndices.raw_path(
            ["1852'", "1815'", f"{str(account_index)}'", str(2), str(key_index)]
        )

    @classmethod
    def drep(cls, account_index: int, key_index: int):
        """Creates derivation indices for drep accounts"""
        return DerivationIndices.raw_path(
            ["1852'", "1815'", f"{str(account_index)}'", str(3), str(key_index)]
        )

    def raw_path(derivation_indices: list[str]):
        """Creates a raw path from derivation indices"""
        return f"m/{'/'.join(derivation_indices)}"
