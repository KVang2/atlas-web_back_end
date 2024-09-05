#!/usr/bin/env python3
"""Basic Caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching"""

    def put(self, key, item):
        """
        adding key-value pair

        Args:
            key: where item is store
            item: value for key

            if key or item is None, does nothing
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get value of the key

        Args:
            key: self.cache_dat is linked to key

        Returns:
            returns value in self.cache_data
            if key is none or doesn't exist return none.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
