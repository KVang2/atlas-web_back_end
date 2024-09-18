#!/usr/bin/env python3
"""
BasicAuth inherits from Auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class inheirts from Auth
    Args:
        Auth (_type_):
    """
    pass

    def extract_base64_authorization_header(
            self, authorization_header: str) ->str:
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
