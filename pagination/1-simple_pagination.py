#!/usr/bin/env python3
"""
simple helper function
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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


def get_page(self, page: int = 1, page_size: int=10) -> List[List]:
    """_summary_

    Args:
        page (_type_): _description_
        page_size (_type_): _description_
    """

    assert isinstance(page, int) and page > 0, "page must be positive integer"
    assert isinstance(page_size, int) and page_size > 0, "page_size must be positive integer"

    start, end = index_range(page, page_size)
    dataset = self.dataset()

    if start >= len(dataset):
        return []

    return dataset[start:end]
