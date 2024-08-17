#!/usr/bin/env python3
"""Class and fuction to implement offset pagination."""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return tuple containing the start index and end index."""
    offset = (page - 1) * page_size
    end = offset + page_size
    return (offset, end)


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
        """Provide requested page elements."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary of important stats."""
        output = self.get_page(page, page_size)
        length = len(self.dataset())
        pages = math.ceil(length / page_size)

        result = {'page_size': len(output),
                  'page': page,
                  'data': output,
                  'next_page': page + 1 if page < pages else None,
                  'prev_page': page - 1 if page > 1 else None,
                  'total_pages': pages}

        return result
