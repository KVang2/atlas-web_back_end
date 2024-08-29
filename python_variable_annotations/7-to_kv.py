#!/usr/bin/env python3

"""
type-annotated function to_kv takes a string, float or int as arguments and returns tuple
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    taking string, int or float and returns a tuple. second element is square of int/float v, annotate as float
    Args:
        k (str): _description_
        v (Union[int, float]): int or float

    Returns:
        Tuple[str, float]: first element is string second element is square of v, annotated as float.
    """
    return k, float(v ** 2)
