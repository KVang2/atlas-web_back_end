#!/usr/bin/env python3
"""
Regexing
"""


from typing import List
import logging
import re


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

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
    redacted_message = re.sub(pattern, lambda match: f"{match.group(1).split('=')[0]}={redaction}", message)
    return redacted_message
