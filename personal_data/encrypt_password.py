#!/usr/bin/env python3
"""
function that returns a salted hased password.
Functions:
    - hash_password:
    - is_valid: expects 2 arguments and returns a boolean
        - args: hashed_passwords: bytes, password: str
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes password using bcrypt
    Args:
        password (str): password to hash

    Returns:
        bytes: salted, hashed password.
    """
    pass_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(pass_bytes, salt)

    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    checking if password matches hashed password.
    Args:
        hashed_password (bytes): hashed password
        password (str): password

    Returns:
        bool: True if password matches
    """
    pass_bytes = password.encode('utf-8')

    return bcrypt.checkpw(pass_bytes, hash)