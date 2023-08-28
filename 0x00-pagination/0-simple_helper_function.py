#!/usr/bin/env python3

"""a module with pagination paramaters as helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """
    Args:
        page: current page number
        page_size: Items displayed per page
    Return:
        A tuple of size tow containing a start and end index
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_data = start_index, end_index
    return tuple(paginated_data)
