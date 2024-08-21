#!/usr/bin/python3
"""class LRUCache that inherits from BaseCaching and is a caching system."""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Actual caching system."""

    def __init__(self):
        """Initialize instance."""
        super().__init__()
        self.times = {}

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return
        self.times.update({key: datetime.now()})
        self.cache_data.update({key: item})

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_used = min(self.times, key=self.times.get)
            self.times.pop(least_used)
            self.cache_data.pop(least_used)
            print(f'DISCARD: {least_used}')

    def get(self, key):
        """Get an item by key."""
        if key in self.times.keys():
            self.times[key] = datetime.now()

        return self.cache_data.get(key, None)
