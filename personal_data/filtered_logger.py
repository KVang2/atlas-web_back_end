#!/usr/bin/env python3
"""
Regexing
"""


from typing import List
import logging
import re

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        init self, redacting formatter
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format method to filter values in incoming log records
        Args:
            record (logging.LogRecord): using filter_datum
            values for fields in fields
        Returns:
            str:
        """
        record_message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION, record_message, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Args:
        fields (List[str]): list of strings representing
        all fields to obfuscate
        redaction (str): str representing
        what field will be obfuscated
        message (str): str representing log line
        separator (str): str representing by which
        character is separating all fields in the log line

    Returns:
        str: redacted log message
    """
    # A regex pattern dynamically to match fields and values
    pattern = '|'.join([rf'({field}=[^{separator}]+)'
                        for field in fields])

    # replace sensitive data with redaction string
    return re.sub(pattern, lambda match:
                  f"{match.group(0).split('=')[0]}={redaction}", message)


def get_logger() -> logging.Logger:
    """
    taking no agrument
    Returns:
        logger
    """
    logger = logging.getLogger("user_data")

    logger.setLevel(logging.INFO)

    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
