#!/usr/bin/env python3
"""module showing basic dictionary for caching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
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
        self.cache_data[key] = item

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
