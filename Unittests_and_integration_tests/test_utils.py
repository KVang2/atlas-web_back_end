#!/usr/bin/env python3
"""
parameterize a unit test, writing the first unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import Mock, patch


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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])

    def test_access_nested_map_exception(self, nested_map, path):
        """
        Parameterize unit test, use assertRaise
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """
    Class, implement testgetjson method to test utils.get_json
    return: expected result
    """
    @patch('utils.requests.get') # patch requests.get to mock HTTP
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    def test_get_json(self, test_url, test_payload, mock_get):
        """
        testing utils.get json
        """
        # create mock object
        mock_obj = Mock()
        mock_obj.json.return_value = test_payload

        mock_get.return_value = mock_obj

        # call get_json
        result = get_json(test_url)

        # Ensure requests.get was called
        mock_get.assert_called_once_with(test_url)

        # Check results matches test payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
