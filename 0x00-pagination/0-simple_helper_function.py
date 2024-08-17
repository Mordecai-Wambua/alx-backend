#!/usr/bin/env python3
"""
Function that two integer arguments.

The function should return a tuple of size two,
 containing a start index and an end index
 corresponding to the range of indexes to return in a list
 for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """Return tuple containing the start index and end index."""
    offset = (page - 1) * page_size
    end = offset + page_size
    return (offset, end)
