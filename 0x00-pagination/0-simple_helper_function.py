#!/usr/bin/env python3
""" simple helper function script"""

from typing import Tuple
""" import Tuple module """

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function that takes two integers to return a tuple """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
