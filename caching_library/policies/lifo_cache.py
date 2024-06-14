from caching_library.cache import Cache
import threading

class LIFOCache(Cache):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.cache = {}
        self.stack = []
        self.lock = threading.Lock()
    
    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                self.cache[key] = value
            else:
                if len(self.cache) >= self.capacity:
                    last_key = self.stack.pop()
                    del self.cache[last_key]
                self.cache[key] = value
                self.stack.append(key)
    
    def get(self, key):
        with self.lock:
            return self.cache.get(key, None)
    
    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                self.stack.remove(key)
    
    def clear(self):
        with self.lock:
            self.cache.clear()
            self.stack.clear()
