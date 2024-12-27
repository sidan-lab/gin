from dataclasses import dataclass


@dataclass
class Network:
    """Equivalent of Go's Network type with constants."""

    TESTNET = "testnet"
    PREVIEW = "preview"
    PREPROD = "preprod"
    MAINNET = "mainnet"

    ALL_NETWORKS = [TESTNET, PREVIEW, PREPROD, MAINNET]

    @staticmethod
    def is_network(value: str) -> bool:
        return value in Network.ALL_NETWORKS
