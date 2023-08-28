#!/usr/bin/env python3
"""FIFOCache Module
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

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
        self.cache_data[key] = item
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.queue.append(key)
        if len(self.queue) > BaseCaching.MAX_ITEMS:
            first_key = self.queue.popleft()
            discarded_item = self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

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
