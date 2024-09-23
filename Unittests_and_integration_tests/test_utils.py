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
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """
        Method to test that it returns what its suppose to
        """
        # check result matches expected value
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
