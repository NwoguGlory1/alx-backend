#!/usr/bin/env python3
""" simple helper function script"""

import csv
import math
from typing import Dict
from typing import List
from typing import Tuple, Union, Optional
""" imports the necessary modules """


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Function that takes two integers to return a tuple"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function to get a specific page of the dataset."""
        assert isinstance(page, int) and page > 0
        "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0
        "Page size must be an integer greater than 0"

        start_index, end_index = self.index_range(page, page_size)

        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, Union[int, List[List], Optional[int]]]:
        """
        method that takes the same arguments (and defaults) as get_page
        Returns a dictionary
        """
        retrieved_data = self.get_page(page, page_size)
        data = retrieved_data
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        dict_result = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return dict_result
