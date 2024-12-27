# flake8: noqa: E501

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Asset:
    unit: str
    quantity: str

    def __repr__(self):
        return f"Asset(unit={self.unit}, quantity={self.quantity})"


@dataclass
class Assets:
    def __init__(self, assets: Optional[List[Asset]] = None):
        self.assets = assets if assets is not None else []

    def get_lovelace(self) -> int:
        """
        Get the 'lovelace' quantity if it exists, otherwise return 0.
        """
        for asset in self.assets:
            if asset.unit == "lovelace":
                try:
                    return int(asset.quantity)
                except ValueError:
                    return 0
        return 0

    def pop_asset_by_unit(self, unit: str) -> Optional[Asset]:
        """
        Pop the first asset with the specified unit and return it.
        """
        for i, asset in enumerate(self.assets):
            if asset.unit == unit:
                pop_asset = self.assets.pop(i)
                return pop_asset
        return None

    def merge_assets(self, assets: List[Asset]) -> List[Asset]:
        """
        Merge new assets into the current assets list. If units match, quantities are added.
        """
        merged_assets = {}
        for asset in self.assets + assets:
            if asset.unit in merged_assets:
                merged_assets[asset.unit].quantity = self.add_quantities(
                    merged_assets[asset.unit].quantity, asset.quantity
                )
            else:
                merged_assets[asset.unit] = asset
        return list(merged_assets.values())

    @staticmethod
    def add_quantities(quantity1: str, quantity2: str) -> str:
        """
        Add two quantities (represented as strings) and return the result as a string.
        """
        try:
            int_quantity1 = int(quantity1)
            int_quantity2 = int(quantity2)
            sum_quantity = int_quantity1 + int_quantity2
            return str(sum_quantity)
        except ValueError:
            return "0"
