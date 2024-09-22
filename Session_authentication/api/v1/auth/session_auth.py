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
            None, session_id
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

    def user_id_for_session_id(
            self, session_id: str = None) -> str:
        """
        instance method that returns user ID based on session ID
        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            None, session_id
        """
        # check if session_id is none
        if session_id is None:
            return None

        # check if session_id is not str
        if not isinstance(session_id, str):
            return None

        # using .get() to access user_id from the session_id
        return self.user_id_by_session_id.get(session_id)
    