#!/usr/bin/env python3
""" Basic dictionary script """
from base_caching import BaseCaching
""" imports BaseCaching class from the .py file"""


class BasicCache(BaseCaching):
    """ class that inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        """ method that add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ method that get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
