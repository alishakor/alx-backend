#!/usr/bin/env python3
"""LIFOCache Module
"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """calling the parent class constructor"""
        super().__init__()
        self.queue = deque()

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
        else:
            if len(self.queue) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    last_key = self.queue.pop()
                    discarded_item = self.cache_data.pop(last_key)
                    print(f"DISCARD: {last_key}")
            self.cache_data[key] = item
            self.queue.append(key)

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
        return self.cache_data[key]
