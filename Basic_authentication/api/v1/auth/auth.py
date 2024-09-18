#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar

# defining generic type for current user
User = TypeVar('User')


class Auth:
    """
    Auth class to manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """
        Public method checking path requires authentication.
        Args:
            path (str): path to check
            excluded_paths (list): list of path

        Returns:
            bool: flase
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Public method that returns none
        Args:
            request (_type_, optional): Flask request object

        Returns:
            str: none
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Public method that returns current user, returning none for now
        Args:
            request: Flask request object
        Returns:
            User: none
        """
        return None
