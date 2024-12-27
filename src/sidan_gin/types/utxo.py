from dataclasses import dataclass
from typing import List, Optional

from sidan_gin.types.asset import Asset


@dataclass
class Input:
    output_index: int
    tx_hash: str


@dataclass
class Output:
    address: str
    amount: List[Asset]
    data_hash: Optional[str] = None
    plutus_data: Optional[str] = None
    script_ref: Optional[str] = None
    script_hash: Optional[str] = None


@dataclass
class UTxO:
    input: Input
    output: Output
