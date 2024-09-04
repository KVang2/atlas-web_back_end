#!/usr/bin/env python3
""" Caching """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """adding key-value pair"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        """Get value"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
    