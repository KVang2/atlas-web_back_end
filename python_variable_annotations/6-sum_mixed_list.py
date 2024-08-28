#!/usr/bin/env python3

"""
type-annotated function sum_mixed_list mixed list of int and float
"""


from typing import Union, List

def sum_mixed_list(mixed_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list, mixed_lst, 
    taking a list of integers and floats and returning the sum as a float
    Args:
        mixed_lst (List[Union[int, float]]): _description_

    Returns:
        float: _description_
    """
    return sum(mixed_lst)
