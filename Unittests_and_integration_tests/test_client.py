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
        ("google"),
        ("abc"),
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

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the correct URL based on the mocked org property.
        """
        # Known payload that will be returned by the mocked 'org' property
        mock_org_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Use patch as a context manager to mock 'GithubOrgClient.org' with PropertyMock
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            # Set the return value for the 'org' property
            mock_org.return_value = mock_org_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Access the _public_repos_url property
            result = client._public_repos_url

            # Check that the _public_repos_url returns the expected URL from the mocked org property
            self.assertEqual(result, "https://api.github.com/orgs/google/repos")

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
