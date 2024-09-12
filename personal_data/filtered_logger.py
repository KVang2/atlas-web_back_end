#!/usr/bin/env python3
"""
Regexing
"""

import re
from typing import List


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
    pattern = '|'.join([rf'({field}=[^|]+)' for field in fields])
    redacted_message = re.sub(pattern, lambda match: match.group(1).split('=')[0] + f'={redaction}', message)
    return redacted_message
