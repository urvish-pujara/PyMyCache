from abc import ABC, abstractmethod

class EvictionPolicy(ABC):
    @abstractmethod
    def evict(self):
        pass
    
    @abstractmethod
    def access(self, key):
        pass
    
    @abstractmethod
    def add(self, key):
        pass
    
    @abstractmethod
    def remove(self, key):
        pass
    
    @abstractmethod
    def clear(self):
        pass
