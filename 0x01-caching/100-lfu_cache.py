#!/usr/bin/env python3
""" LFU caching script """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.freq = {}
        self.freq_list = {}
        self.min_freq = 0

    def _update_frequency(self, key):
        """ Update the frequency of the accessed key """
        freq = self.freq[key]
        self.freq[key] += 1

        # Remove the key from the old frequency list
        self.freq_list[freq].remove(key)
        if not self.freq_list[freq]:
            del self.freq_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add the key to the new frequency list
        if self.freq[key] not in self.freq_list:
            self.freq_list[self.freq[key]] = []
        self.freq_list[self.freq[key]].append(key)

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the least frequently used key
            lfu_key = self.freq_list[self.min_freq].pop(0)
            del self.cache_data[lfu_key]
            del self.freq[lfu_key]
            if not self.freq_list[self.min_freq]:
                del self.freq_list[self.min_freq]

            print(f"DISCARD: {lfu_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item
        self.freq[key] = 1
        self.min_freq = 1
        if self.min_freq not in self.freq_list:
            self.freq_list[self.min_freq] = []
        self.freq_list[self.min_freq].append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)
        return self.cache_data[key]
