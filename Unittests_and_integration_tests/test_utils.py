#!/usr/bin/env python3
"""
parameterize a unit test, writing the first unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Method to test that it returns what its suppose to
        """
        # check result matches expected value
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])

    def test_access_nested_map_exception(self, nested_map, path):
        """
        Parameterize unit test, use assertRaise
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

if __name__ == '__main__':
    unittest.main()
