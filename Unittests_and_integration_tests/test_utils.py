#!/usr/bin/env python3
"""
parameterize a unit test, writing the first unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    def test_get_json(self, test_url, test_payload):
        """
        testing utils.get json
        """
        with patch('utils.requests.get') as mock_get:
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

class TestMomize(unittest.TestCase):
    """
    implement Testmemoise class with test_memoize method
    """

    def test_memoize(self):
        """
        using mock.patch to mock method,
        test a_property when called twice correct result is return
        a_method called once using assert_called_once
        """
        class TestClass:
            """
            def a_method(self):
                return: 42
            def a_property(self):
                return self.a_method()
            """

            def a_method(self):
                """
                mock a_method to track calls
                """
                return 42

            @memoize
            def a_property(self):
                """
                all a_property of Testclass twice,
                compute result by calling a_mthod.
                Returns:
                    cached result
                """
                return self.a_method()

        test_instance = TestClass()

        with patch('TestClass.a_method') as mock_a_method:
            # access a_property twice
            access1 = test_instance.a_property
            access2 = test_instance.a_property

            # Check return values are correct
            self.assertEqual(access1, 42)
            self.assertEqual(access2, 42)

            # Make sure a_method was called once
            mock_a_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
