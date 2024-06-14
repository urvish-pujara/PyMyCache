from collections import OrderedDict
from caching_library.cache import Cache
import threading

class LRUCache(Cache):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lock = threading.Lock()
    
    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    
    def get(self, key):
        with self.lock:
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            return None
    
    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
    
    def clear(self):
        with self.lock:
            self.cache.clear()
