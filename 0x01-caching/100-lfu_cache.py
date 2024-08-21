#!/usr/bin/python3
"""class LFUCache that inherits from BaseCaching and is a caching system."""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Actual caching system."""

    def __init__(self):
        """Initialize instance."""
        super().__init__()
        self.times = {}

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                checker = sorted(self.times, key=self.times.get)
                least_used = checker[0]
                self.times.pop(least_used)
                self.cache_data.pop(least_used)
                print(f'DISCARD: {least_used}')
            self.cache_data.update({key: item})
            self.times.update({key: 0})
        else:
            self.cache_data.update({key: item})
            self.times[key] += 1

    def get(self, key):
        """Get an item by key."""
        if key in self.times.keys():
            self.times[key] += 1

        return self.cache_data.get(key, None)
