#!/usr/bin/env python3
"""LFUCache Module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LRUache class that inherits from BaseCaching"""

    def __init__(self):
        """calling the parent class constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Args:
            key(str): Cache dictionary key
            item(Any): Cache key value
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Getting key from the ordered dict
                k, v = self.cache_data.popitem()
                print(f"DISCARD: {k}")
            # Adding the key-value pair to the dict
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Arg:
            key(str): Cache dictionary key

        Return:
            None if key is None or not in self.cache_data else
            return self.cache_data[key]
        """
        if key is not None or key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data.get(key, None)
