#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFO caching that inherits from baseCaching
    """

    def __init__(self):
        """
        calling parent class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign self.cache_data item value for key
        Args:
            key (_type_): _description_
            item (_type_): _description_
        Return:
            if key or item is None, don't do anything
        """
        if key is None:
            return
        
        if item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            # remove the first key inserted
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f'DISCARD: {oldest_key}')
        
        # Adding or updating the cache with new key and item
        self.cache_data[key] = item

        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """
        returning value in self.cache_data linked to key
        Args:
            key (_type_):
        Return:
            return value linked to key
            if key is none or doesn't exist in
            self.cache_data return None
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
