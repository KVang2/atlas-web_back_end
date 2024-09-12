#!/usr/bin/env python3
"""
Regexing
"""


from typing import List
import logging
import re

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Args:
        fields (List[str]): _description_
        redaction (str): _description_
        message (str): _description_
        separator (str): _description_

    Returns:
        str: _description_
    """
    pattern = '|'.join([rf'({field}=[^{separator}]+)' for field in fields])

    return re.sub(pattern, lambda match: f"{match.group(0).split('=')[0]}={redaction}", message)
