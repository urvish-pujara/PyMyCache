from collections import deque
from caching_library.cache import Cache
import threading

class FIFOCache(Cache):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()
        self.lock = threading.Lock()
    
    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                self.cache[key] = value
            else:
                if len(self.cache) >= self.capacity:
                    oldest_key = self.queue.popleft()
                    del self.cache[oldest_key]
                self.cache[key] = value
                self.queue.append(key)
    
    def get(self, key):
        with self.lock:
            return self.cache.get(key, None)
    
    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                self.queue.remove(key)
    
    def clear(self):
        with self.lock:
            self.cache.clear()
            self.queue.clear()
