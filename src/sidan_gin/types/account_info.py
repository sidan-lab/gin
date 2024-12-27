from dataclasses import dataclass
from typing import Optional


@dataclass
class AccountInfo:
    active: bool
    pool_id: Optional[str]
    balance: str
    rewards: str
    withdrawals: str
