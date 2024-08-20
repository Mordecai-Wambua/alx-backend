#!/usr/bin/python3
"""class LIFOCache that inherits from BaseCaching and is a caching system."""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
            checker = sorted(self.times, key=self.times.get, reverse=True)
            latest = checker[1]
            self.times.pop(latest)
            self.cache_data.pop(latest)
            print(f'DISCARD: {latest}')

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
