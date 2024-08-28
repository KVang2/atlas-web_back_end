#!/usr/bin/env python3

"""
type-annotated function make_multiplier that takes float multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """

    Args:
        multiplier (float):

    Returns:
        a function that multiplies a float by multiplier
        lambda function takes a float and returns it muliplied by the multiplier.
    """
    return lambda x: x * multiplier
