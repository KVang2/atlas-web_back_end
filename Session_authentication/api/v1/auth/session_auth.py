#!/usr/bin/env python3
"""
class session Auth inherits from Auth
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session authentication class that inherits
    Args:
        Auth (_type_):
    """

    # class attribute initialized by empty dic
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creating session ID for user_id
        Args:
            user_id (str, optional): checking if it is None or not a string

        Returns:
            None
        """
        # Check if user_id is none
        if user_id is None:
            return

        # check if user_id is not a str
        if not isinstance(user_id, str):
            return None

        # store session Id as key and user_id as value
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
