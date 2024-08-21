#!/usr/bin/python3
"""class MRUCache that inherits from BaseCaching and is a caching system."""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
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
            checker = sorted(self.times, key=self.times.get, reverse=True)
            most_recent = checker[1]
            self.times.pop(most_recent)
            self.cache_data.pop(most_recent)
            print(f'DISCARD: {most_recent}')

    def get(self, key):
        """Get an item by key."""
        if key in self.times.keys():
            self.times[key] = datetime.now()

        return self.cache_data.get(key, None)
