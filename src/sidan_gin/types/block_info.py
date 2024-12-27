from dataclasses import dataclass


@dataclass
class BlockInfo:
    time: int
    hash: str
    slot: str
    epoch: int
    epoch_slot: str
    slot_leader: str
    size: int
    tx_count: int
    output: str
    fees: str
    previous_block: str
    next_block: str
    confirmations: int
    operational_certificate: str
    vrf_key: str
