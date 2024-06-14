from caching_library.cache import Cache
from caching_library.eviction_policy import EvictionPolicy
import threading

class CustomCache(Cache):
    def __init__(self, capacity, eviction_policy: EvictionPolicy):
        super().__init__()
        self.capacity = capacity
        self.cache = {}
        self.eviction_policy = eviction_policy
        self.lock = threading.Lock()
    
    def set(self, key, value):
        with self.lock:
            if key in self.cache:
                self.cache[key] = value
            else:
                if len(self.cache) >= self.capacity:
                    key_to_evict = self.eviction_policy(self.cache)
                    del self.cache[key_to_evict]
                self.cache[key] = value
    
    
    def get(self, key):
        with self.lock:
            return self.cache.get(key, None)
    
    def delete(self, key):
        with self.lock:
            if key in self.cache:
                self.eviction_policy.remove(key)
                del self.cache[key]
    
    def clear(self):
        with self.lock:
            self.cache.clear()
            self.eviction_policy.clear()
