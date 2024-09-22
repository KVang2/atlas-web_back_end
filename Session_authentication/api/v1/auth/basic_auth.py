#!/usr/bin/env python3
"""
BasicAuth inherits from Auth
"""

import base64
import binascii
from models.user import User
from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """
    BasicAuth class inheirts from Auth
    Args:
        Auth (_type_):
    """
    pass

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Method that returns Base64 part of Authorization header
        for basic authentication:
        Args:
            authorization_header (str): header

        Returns:
            Base64 parts
            None: if authorization_header is None, not a string,
                doesnt start by Basic
                return value after basic.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        method that returns decoded value of a Base64 str
        Args:
            base64_authorization_header (str):

        Returns:
            None: if base64_authorization is none
                if is not string
                if not a valid Base64
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            base_auth = base64.b64decode(
                base64_authorization_header, validate=True)

            return base_auth.decode('utf-8')

        except (binascii.Error, ValueError, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        method that returns user email and password from Base64 decoded value.
        Args:
            self (_type_): value 1
            str (_type_): value 2
        Returns:
            (str, str): contains user email and password
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_e, user_pw = decoded_base64_authorization_header.split(':', 1)

        return user_e, user_pw

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        method that returns user instance based on email and password
        Args:
            self (_type_): _description_
        """
        if user_email is None or user_pwd is None:
            return None

        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})

            if not users:
                return None

            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

        except Exception as error:
            return None
