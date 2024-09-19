#!/usr/bin/env python3
"""
BasicAuth inherits from Auth
"""

import re
import base64
import binascii
from api.v1.auth.auth import Auth


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
        
        user_email, user_password = decoded_base64_authorization_header.split(':', 1)

        return user_email, user_password

        