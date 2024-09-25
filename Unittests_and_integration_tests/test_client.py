#!/usr/bin/env python3
"""
parameterize and patch decorators
delcare TestGithubOrgclient(unittest.TestCase)
implement test_org, test GithubOrgClient.org   
"""

import unittest
from unittest.mock import patch
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
        # set client
        client = GithubOrgClient(org_name)

        # call org method
        client.org

        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    @patch('GithubOrgClient.org')
    def test_public_repos_url(self, mock):
        """
        Test property return
            mock
        """
        # Mock return value for org
        mock.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # create instance of GithubOrgCLient
        client = GithubOrgClient("google")

        # access publci repos url property
        result = client._public_respo_url

        # Assert public repos url is expected value
        mock.assert_called_once()
