#!/usr/bin/env python3
"""LRUCache Module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUache class that inherits from BaseCaching"""

    def __init__(self):
        """calling the parent class constructor"""
        super().__init__()
        self.data = OrderedDict()

    def put(self, key, item):
        """
        Args:
            key(str): Cache dictionary key
            item(Any): Cache key value

        Return:
            None
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.data[key]  = item
            self.data.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Getting the first key from the ordered dict
                removed_key = next(iter(self.data))
                # pop the key from both dictionaries
                print(f"DISCARD: {removed_key}")
                self.cache_data.pop(removed_key)
                self.data.pop(removed_key)
            # Adding the key-value pair to the dictionaries
            self.cache_data[key] = item
            self.data[key] = item
            self.data.move_to_end(key)

    def get(self, key):
        """
        Arg:
            key(str): Cache dictionary key

        Return:
            None if key is None or not in self.cache_data else
            return self.cache_data[key]
        """
        if key is None or key not in self.cache_data:
            return None
        elif key in self.data:
            self.data.move_to_end(key)
            return self.cache_data[key]
