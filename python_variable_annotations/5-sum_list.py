#!/usr/bin/env python3

"""
type-annotated function sum_list list of floats
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum list

    Args:
        input_list (List[float]):

    Returns:
        float: sum(input_list)
    """
    return sum(input_list)
