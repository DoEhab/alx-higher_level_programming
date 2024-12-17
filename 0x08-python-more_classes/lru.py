class LRUCache:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end()
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end()

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            cache.popitem()

