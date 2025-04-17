class DerivationIndices:
    @classmethod
    def default(cls):
        """Default derivation indices (payment with index 0)"""
        return DerivationIndices.payment(0, 0)

    @classmethod
    def payment(cls, account_index: int, key_index: int):
        """Creates derivation indices for payment accounts"""
        return [1852, 1815, account_index, 0, key_index]

    @classmethod
    def stake(cls, account_index: int, key_index: int):
        """Creates derivation indices for stake accounts"""
        return [1852, 1815, account_index, 2, key_index]

    @classmethod
    def drep(cls, account_index: int, key_index: int):
        """Creates derivation indices for drep accounts"""
        return [1852, 1815, account_index, 3, key_index]
