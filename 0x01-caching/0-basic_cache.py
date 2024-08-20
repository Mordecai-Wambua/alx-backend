#!/usr/bin/python3
"""class BasicCache that inherits from BaseCaching and is a caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Actual Caching System."""

    def __init__(self):
        """Initialize the instance."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            pass
        self.cache_data.update({key: item})

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
