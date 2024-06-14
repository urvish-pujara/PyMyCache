import argparse
from caching_library.policies.fifo_cache import FIFOCache
from caching_library.policies.lru_cache import LRUCache
from caching_library.policies.lifo_cache import LIFOCache
from caching_library.policies.custom_cache import CustomCache
import json
import os

def load_cache(filename, cache):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                for key, value in data.items():
                    cache.set(key, value)
            except json.JSONDecodeError:
                pass  # Handle empty or invalid JSON file

def save_cache(filename, cache):
    with open(filename, 'w') as file:
        json.dump(cache.cache, file)

def get_custom_eviction_function():
    print("Define your custom eviction function. The function should accept a dictionary (cache) and return a key to evict.")
    custom_code = input("Enter your custom eviction function code (lambda function): ")
    try:
        eviction_function = eval(custom_code)
        return eviction_function
    except Exception as e:
        print(f"Error in defining custom eviction function: {e}")
        return None

def main():
    print("Enter your cache policy: FIFO, LRU, LIFO, CUSTOM and capacity separated by space")
    policy = input("").split()
    if policy[0].upper() == "FIFO":
        cache = FIFOCache(int(policy[1]))
    elif policy[0].upper() == "LRU":
        cache = LRUCache(int(policy[1]))
    elif policy[0].upper() == "LIFO":
        cache = LIFOCache(int(policy[1]))
    elif policy[0].upper() == "CUSTOM":
        eviction_function = get_custom_eviction_function()
        if eviction_function is None:
            print("Invalid custom eviction function. Exiting.")
            return
        cache = CustomCache(int(policy[1]), eviction_function)
    else:
        print("Invalid policy")
        return

    # Load initial cache state from cache.txt
    load_cache('cache.txt', cache)

    print("Action syntax: Set(key,value) Get(key) Delete(key) Clear() Exit()")
    while True:
        choice = input("")
        if choice == "Exit()":
            # Save final cache state to cache.txt
            save_cache('cache.txt', cache)
            break
        elif choice == "Clear()":
            cache.clear()
            print("Cache cleared")
        elif choice.startswith("Set(") and choice.endswith(")"):
            key, value = choice[4:-1].split(',')
            cache.set(key, value)
            print(f"Key {key} set to {value}")
        elif choice.startswith("Get(") and choice.endswith(")"):
            key = choice[4:-1]
            value = cache.get(key)
            print(f"Value for key {key}: {value}")
        elif choice.startswith("Delete(") and choice.endswith(")"):
            key = choice[7:-1]
            cache.delete(key)
            print(f"Key {key} deleted")
        else:
            print("Invalid action")

if __name__ == '__main__':
    main()
