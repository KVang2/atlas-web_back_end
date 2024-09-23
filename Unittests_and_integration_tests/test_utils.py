#!/usr/bin/env python3
"""
parameterize a unit test, writing the first unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand([
        ("nested_map", {"a": 1}, ("a",), 1),
        ("nested_map2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("nested_map3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_accesss_nested_map(self, name, nested_map, path, expected):
        """
        Method to test that it returns what its suppose to
        """
        # call access_nested_map function
        result = access_nested_map(nested_map, path)

        # check result matches expected value
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()