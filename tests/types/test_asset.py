import unittest

from sidan_gin import Asset, Assets  # Replace with the actual import path


class TestAssetsMethods(unittest.TestCase):
    def test_get_lovelace(self):
        # Test case 1: assets containing "lovelace"
        assets = Assets(
            [Asset(unit="lovelace", quantity="100"), Asset(unit="USD", quantity="100")]
        )
        self.assertEqual(assets.get_lovelace(), 100)

        # Test case 2: assets not containing "lovelace"
        assets = Assets([Asset(unit="USD", quantity="100")])
        self.assertEqual(assets.get_lovelace(), 0)

        # Test case 3: nil assets (empty list)
        assets = Assets()
        self.assertEqual(assets.get_lovelace(), 0)

    def test_pop_asset_by_unit(self):
        # Define test cases
        test_cases = [
            {
                "name": "Pop existing asset",
                "initial_assets": [
                    Asset(unit="lovelace", quantity="1000"),
                    Asset(unit="asset1", quantity="2000"),
                    Asset(unit="asset2", quantity="3000"),
                ],
                "unit_to_pop": "asset1",
                "expected_asset": Asset(unit="asset1", quantity="2000"),
                "expected_assets": [
                    Asset(unit="lovelace", quantity="1000"),
                    Asset(unit="asset2", quantity="3000"),
                ],
            },
            {
                "name": "Pop non-existing asset",
                "initial_assets": [
                    Asset(unit="lovelace", quantity="1000"),
                    Asset(unit="asset1", quantity="2000"),
                    Asset(unit="asset2", quantity="3000"),
                ],
                "unit_to_pop": "asset3",
                "expected_asset": None,  # Python equivalent of Go's empty asset
                "expected_assets": [
                    Asset(unit="lovelace", quantity="1000"),
                    Asset(unit="asset1", quantity="2000"),
                    Asset(unit="asset2", quantity="3000"),
                ],
            },
        ]

        for case in test_cases:
            with self.subTest(name=case["name"]):
                assets = Assets(case["initial_assets"])
                popped_asset = assets.pop_asset_by_unit(case["unit_to_pop"])

                # Assert the popped asset matches the expected asset
                if case["expected_asset"] is None:
                    self.assertIsNone(popped_asset)
                else:
                    self.assertEqual(popped_asset, case["expected_asset"])

                # Assert the remaining assets match the expected assets
                self.assertListEqual(assets.assets, case["expected_assets"])


if __name__ == "__main__":
    unittest.main()
