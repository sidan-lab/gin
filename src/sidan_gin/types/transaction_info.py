from dataclasses import dataclass


@dataclass
class TransactionInfo:
    index: int
    block: str
    hash: str
    slot: str
    fees: str
    size: int
    deposit: str
    invalid_before: str
    invalid_after: str
