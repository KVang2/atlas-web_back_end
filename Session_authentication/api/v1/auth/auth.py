#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar
import os

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
        if path is None:
            return True

        if excluded_paths is None:
            return True

        if path is excluded_paths:
            return False

        # ensure path has trailing slash
        if path[-1] != '/':
            path += '/'

        # If path matches path in excluded paths
        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'

            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Public method that returns none
        Args:
            request (_type_, optional): Flask request object

        Returns:
            str: none
        """
        # checking authorization header exist
        if request is None:
            return None

        # if request contain header key return value of header
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """
        Public method that returns current user, returning none for now
        Args:
            request: Flask request object
        Returns:
            User: none
        """
        return None

    def session_cookie(self, request=None):
        """
        returns cookie value from a request
        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        # return none if request is none
        if request is None:
            return None

        # Get cookie name from environment var session
        session_name = os.getenv('SESSION_NAME', 'my_session_id')

        # Get session ID from cookie
        return request.cookies.get(session_name)
