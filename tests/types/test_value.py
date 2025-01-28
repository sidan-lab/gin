# flake8: noqa: E501
import unittest

from sidan_gin import Asset, Value  # Adjust import path based on your project structure


class TestValue(unittest.TestCase):

    def test_add_asset(self):
        asset = Asset(unit="USD", quantity="100")
        mv = Value().add_asset(asset)
        self.assertEqual(mv.get("USD"), 100, f"Expected 100, got {mv.get('USD')}")

    def test_add_assets(self):
        assets = [Asset(unit="USD", quantity="100"), Asset(unit="EUR", quantity="200")]
        mv = Value().add_assets(assets)
        self.assertEqual(mv.get("USD"), 100, f"Expected 100, got {mv.get('USD')}")
        self.assertEqual(mv.get("EUR"), 200, f"Expected 200, got {mv.get('EUR')}")

    def test_negate_asset(self):
        asset = Asset(unit="USD", quantity="100")
        mv = Value().add_asset(asset).negate_asset(asset)
        self.assertEqual(mv.get("USD"), 0, f"Expected 0, got {mv.get('USD')}")

    def test_negate_assets(self):
        assets = [Asset(unit="USD", quantity="100"), Asset(unit="EUR", quantity="200")]
        mv = Value().add_assets(assets).negate_assets(assets)
        self.assertEqual(mv.get("USD"), 0, f"Expected 0, got {mv.get('USD')}")
        self.assertEqual(mv.get("EUR"), 0, f"Expected 0, got {mv.get('EUR')}")

    def test_merge(self):
        mv1 = Value().add_asset(Asset(unit="USD", quantity="100"))
        mv2 = Value().add_asset(Asset(unit="USD", quantity="200")).merge(mv1)
        self.assertEqual(mv2.get("USD"), 300, f"Expected 300, got {mv2.get('USD')}")

    def test_merge_nil(self):
        mv1 = Value().add_asset(Asset(unit="USD", quantity="100"))
        mv1.merge(None)
        self.assertEqual(mv1.get("USD"), 100, f"Expected 100, got {mv1.get('USD')}")

    def test_merge_from_new_map(self):
        mv1 = Value().add_asset(Asset(unit="USD", quantity="100"))
        mv2 = Value().merge(mv1)
        self.assertEqual(mv2.get("USD"), 100, f"Expected 100, got {mv2.get('USD')}")

    def test_to_assets(self):
        mv = Value().add_asset(Asset(unit="USD", quantity="100"))
        assets = mv.to_assets()
        self.assertEqual(len(assets), 1, f"Expected 1 asset, got {len(assets)}")
        self.assertEqual(
            assets[0].unit, "USD", f"Expected Unit 'USD', got {assets[0].unit}"
        )
        self.assertEqual(
            assets[0].quantity,
            "100",
            f"Expected Quantity '100', got {assets[0].quantity}",
        )

    def test_from_assets(self):
        assets = [Asset(unit="USD", quantity="100"), Asset(unit="EUR", quantity="200")]
        mv = Value.from_assets(assets)
        self.assertEqual(mv.get("USD"), 100, f"Expected 100, got {mv.get('USD')}")
        self.assertEqual(mv.get("EUR"), 200, f"Expected 200, got {mv.get('EUR')}")

    def test_geq(self):
        # Define test cases
        test_cases = [
            {
                "name": "Value1 greater than or equal to Value2",
                "value1": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                    ]
                ),
                "value2": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="500"),
                        Asset(unit="asset2", quantity="1500"),
                    ]
                ),
                "expected": True,
            },
            {
                "name": "Value1 less than Value2",
                "value1": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="1000"),
                    ]
                ),
                "value2": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1500"),
                        Asset(unit="asset2", quantity="1500"),
                    ]
                ),
                "expected": False,
            },
            {
                "name": "Value1 equal to Value2",
                "value1": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                    ]
                ),
                "value2": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                    ]
                ),
                "expected": True,
            },
            {
                "name": "Value1 has more assets than Value2",
                "value1": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                        Asset(unit="asset3", quantity="3000"),
                    ]
                ),
                "value2": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                    ]
                ),
                "expected": True,
            },
            {
                "name": "Value1 has fewer assets than Value2",
                "value1": Value.from_assets([Asset(unit="asset1", quantity="1000")]),
                "value2": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                    ]
                ),
                "expected": False,
            },
            {
                "name": "Value1 has fewer assets than Value2",
                "value1": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1500"),
                        Asset(unit="asset2", quantity="1500"),
                    ]
                ),
                "value2": Value.from_assets(
                    [
                        Asset(unit="asset1", quantity="1000"),
                        Asset(unit="asset2", quantity="2000"),
                    ]
                ),
                "expected": False,
            },
        ]

        for case in test_cases:
            with self.subTest(case["name"]):
                self.assertEqual(
                    case["value1"].geq(case["value2"]), case["expected"], case["name"]
                )


if __name__ == "__main__":
    unittest.main()
