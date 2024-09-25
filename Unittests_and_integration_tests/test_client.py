#!/usr/bin/env python3
"""
parameterize and patch decorators
delcare TestGithubOrgclient(unittest.TestCase)
implement test_org, test GithubOrgClient.org   
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    test GithubOrgClient.org, to return correct value.
    Use @patch, called get_json once with expected arg
    but not executed.
    @parameterized.exand, parametrize test with org examples,
    to pass GithubOrgClient
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        user decorator patch, parameterized.expand
        test org example (google, abc) to pass Github
        """
        # Define a mock response object
        mock_obj = {
            "login": org_name,
            "id": 12345,
            "url": f"https://api.github.com/orgs/{org_name}"
        }
        mock_get_json.return_value = mock_obj

        # set client
        client = GithubOrgClient(org_name)

        # call org method
        result = client.org()

        # check get_json was called correct
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # check that result matches mock obj
        self.assertEqual(result, mock_obj)


if __name__ == '__main__':
    unittest.main()
