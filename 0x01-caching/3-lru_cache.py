#!/usr/bin/env python3
""" LRU caching script """
from base_caching import BaseCaching
""" imports BaseCaching class from the .py file"""


class LRUCache(BaseCaching):
    """ class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.order = []
        """ keeps track of the order in which keys are added to cache"""

    def put(self, key, item):
        """ method that add a new item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
            """ remove key if it already exists"""
        # self.cache_data is a dictionary. It stores the cached items
        # Each item is associated with a unique key.

        self.cache_data[key] = item
        # Add the new key-value pair to the cache
        self.order.append(key)
        # Add the key to the order list

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recently_used_key = self.order.pop(0)
            # Removes least recently used key located at begining of self.order
            del self.cache_data[least_recently_used_key]
            # Remove newest key value pair
            print(f"DISCARD: {least_recently_used_key}")

    def get(self, key):
        """ method that get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
