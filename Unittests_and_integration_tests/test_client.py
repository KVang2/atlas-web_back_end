#!/usr/bin/env python3
"""
parameterize and patch decorators
delcare TestGithubOrgclient(unittest.TestCase)
implement test_org, test GithubOrgClient.org   
"""

import unittest
from unittest.mock import PropertyMock, patch
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
        

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test property return
            mock
        """
        # Mock return value for org
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # create instance of GithubOrgCLient
        client = GithubOrgClient("google")

        # access public repos url property
        result = client._public_repos_url

        # Assert public url to expected value
        self.assertEqual("https://api.github.com/orgs/google/repos", result)

        # Assert public repos url is expected value
        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test public repos
        test that list repos is what expected from chosen payload
        test mocked property and mocked get_json
        """
        # Define payload that get_json
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_repos_payload

        # Mock _public_repos_url using a context manager
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call public_repos method
            result = client.public_repos()

            # Assert that the list of repo names matches the expected list
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Assert that _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

            # Assert that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has license
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)
