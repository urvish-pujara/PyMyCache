from abc import ABC, abstractmethod

class Cache(ABC):
    @abstractmethod
    def set(self, key, value):
        pass
    
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass
    
    @abstractmethod
    def clear(self):
        pass
