# flake8: noqa: E501

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Asset:
    unit: str
    quantity: str  # Stored as a string for compatibility with Cardano data


class Value:
    def __init__(self):
        # Represents the value map where the key is the asset name and the value is the quantity
        self.value: Dict[str, int] = {}

    @staticmethod
    def from_assets(assets: Optional[List[Asset]]) -> "Value":
        """Create a new Value instance with the given assets."""
        value = Value()
        if assets is None:
            return value
        return value.add_assets(assets)

    def add_asset(self, asset: Asset) -> "Value":
        """Add an asset to the Value class's value record."""
        quantity = int(asset.quantity)
        if asset.unit in self.value:
            self.value[asset.unit] += quantity
        else:
            self.value[asset.unit] = quantity
        return self

    def add_assets(self, assets: List[Asset]) -> "Value":
        """Add multiple assets to the Value class's value record."""
        for asset in assets:
            self.add_asset(asset)
        return self

    def negate_asset(self, asset: Asset) -> "Value":
        """Deduct the value amount of an asset from the Value class's value record."""
        if asset is None:
            return self
        quantity = int(asset.quantity)
        if asset.unit in self.value:
            new_quantity = self.value[asset.unit] - quantity
            if new_quantity <= 0:
                del self.value[asset.unit]
            else:
                self.value[asset.unit] = new_quantity
        return self

    def negate_assets(self, assets: List[Asset]) -> "Value":
        """Deduct the value amount of multiple assets from the Value class's value record."""
        for asset in assets:
            self.negate_asset(asset)
        return self

    def merge(self, *values: "Value") -> "Value":
        """Merge multiple Value class's value record into the current Value class's value record."""
        for other in values:
            if other is None:
                continue
            for unit, quantity in other.value.items():
                if unit in self.value:
                    self.value[unit] += quantity
                else:
                    self.value[unit] = quantity
        return self

    def get(self, unit: str) -> int:
        """Get the quantity of an asset in the Value class's value record."""
        return self.value.get(unit, 0)

    def units(self) -> List[str]:
        """Get the list of asset names in the Value class's value record."""
        return list(self.value.keys())

    def is_empty(self) -> bool:
        """Check if the Value class's value record is empty."""
        return len(self.value) == 0

    def to_assets(self) -> List[Asset]:
        """Convert the Value class's value record into a list of Asset."""
        return [
            Asset(unit=unit, quantity=str(quantity))
            for unit, quantity in self.value.items()
        ]

    def geq(self, other: "Value") -> bool:
        """Check if the value is greater than or equal to another value."""
        for unit, quantity in other.value.items():
            if self.value.get(unit, 0) < quantity:
                return False
        return True
