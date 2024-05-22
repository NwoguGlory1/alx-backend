#!/usr/bin/env python3
""" FIFO caching script """
from base_caching import BaseCaching
""" imports BaseCaching class from the .py file"""


class FIFOCache(BaseCaching):
    """ class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ method that add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
            """ remove key if it already exists"""
        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_firstkey = self.order.pop(0)
            del self.cache_data[oldest_firstkey]
            print(f"DISCARD: {oldest_firstkey}")

    def get(self, key):
        """ method that get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
