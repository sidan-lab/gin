from dataclasses import dataclass


@dataclass
class Protocol:
    epoch: int
    min_fee_a: int
    min_fee_b: int
    max_block_size: int
    max_tx_size: int
    max_block_header_size: int
    key_deposit: int
    pool_deposit: int
    decentralisation: float
    min_pool_cost: str
    price_mem: float
    price_step: float
    max_tx_ex_mem: str
    max_tx_ex_steps: str
    max_block_ex_mem: str
    max_block_ex_steps: str
    max_val_size: int
    collateral_percent: int
    max_collateral_inputs: int
    coins_per_utxo_size: int
    min_fee_ref_script_cost_per_byte: int
