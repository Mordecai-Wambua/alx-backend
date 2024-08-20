#!/usr/bin/python3
"""class FIFOCache that inherits from BaseCaching and is a caching system."""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Actual caching system."""

    def __init__(self):
        """Initialize instance."""
        super().__init__()
        self.times = {}

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
        self.times.update({key: datetime.now()})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest = min(self.times, key=self.times.get)
            self.times.pop(oldest)
            self.cache_data.pop(oldest)
            print(f'DISCARD: {oldest}')

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
