#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary of important stats."""
        assert index is None or (0 <= index < len(self.dataset()))

        start = index if not None else 0

        data = []
        dataset = self.indexed_dataset()
        dataset_length = len(dataset)
        temp_index = start

        while len(data) < page_size and temp_index < dataset_length:
            if temp_index in dataset:
                data.append(dataset[temp_index])
            temp_index += 1

        next_index = temp_index if temp_index < dataset_length else None

        return {
            'index': start,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
            }
