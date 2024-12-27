import unittest

from sidan_gin import Network  # Adjust the import path to match your project structure


class TestNetwork(unittest.TestCase):
    def test_constants(self):
        # Test that network constants are defined correctly
        self.assertEqual(Network.TESTNET, "testnet")
        self.assertEqual(Network.PREVIEW, "preview")
        self.assertEqual(Network.PREPROD, "preprod")
        self.assertEqual(Network.MAINNET, "mainnet")

    def test_all_networks(self):
        # Test that ALL_NETWORKS contains all defined networks
        expected_networks = ["testnet", "preview", "preprod", "mainnet"]
        self.assertListEqual(Network.ALL_NETWORKS, expected_networks)

    def test_is_network(self):
        # Test that is_network returns True for valid networks
        self.assertTrue(Network.is_network("testnet"))
        self.assertTrue(Network.is_network("preview"))
        self.assertTrue(Network.is_network("preprod"))
        self.assertTrue(Network.is_network("mainnet"))

        # Test that is_network returns False for invalid networks
        self.assertFalse(Network.is_network("invalid"))
        self.assertFalse(Network.is_network("abc"))
        self.assertFalse(Network.is_network(""))


if __name__ == "__main__":
    unittest.main()
