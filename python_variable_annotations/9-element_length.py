#!/usr/bin/env python3

"""
type-annotated function iterable object, annotate function's parameters
"""


from typing import List, Tuple, Sequence, Iterable, Any


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    iterable object
    Args:
        lst (Sequence[str]):

    Returns:
        List[Tuple[str, int]]:
    """
    return [(i, len(i)) for i in lst]
