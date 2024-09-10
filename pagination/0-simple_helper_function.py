#!/usr/bin/env python3
"""
simple helper function
"""

def index_range(page, page_size):
    """
    Function taking two int arguments
    Args:
        page (int): Current page number
        page_size (int): Number of items per page
    Return:
        tuple of size two containing start index and an ed index
        corresponding to range of index
        return list for particular pagination
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be greater than 0")

    # calculate starting index for given page
    start = (page - 1) * page_size

    # calculate ending index for given page
    end = start + page_size

    return (start, end)
