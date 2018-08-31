# https://leetcode.com/problems/lru-cache/description/
from collections import deque


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d_cache = {}
        self.lru_cache = deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d_cache:
            return -1
        else:
            self.lru_cache.remove(key)
            self.lru_cache.appendleft(key)
            return self.d_cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        self.d_cache.update({key: value})
        if len(self.d_cache) > self.capacity:
            # remove lru
            self.d_cache.pop(self.lru_cache.pop())

        try:
            self.lru_cache.remove(key)
        except ValueError:
            pass
        self.lru_cache.appendleft(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
