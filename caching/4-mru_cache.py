#!/usr/bin/env python3
"""LRU CACHING"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache
    Args:
        BaseCaching
    """

    def __init__(self):
        """
        calling parent class BaseCaching 
        """
        super().__init__()
        self.order = []
    
    def put(self, key, item):
        """
        Assign self.cache_data
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None:
            return
        
        if item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            MRU_key = self.order.pop()
            del self.cache_data[MRU_key]
            print(f'DISCARD: {MRU_key}')
    
        self.cache_data[key] = item
        self.order.append(key)

        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """
        returning value in self.cache_data linked to key
        Args:
            key (_type_): _description_
        """
        if key is None:
            return
        return self.cache_data.get(key)
    