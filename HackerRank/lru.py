from collections import MutableMapping, OrderedDict
class LruCache(MutableMapping):

    def __init__(self, max_size=10, *args, **kwargs):
        self.max_size = max_size
        self.store = OrderedDict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        # Move the key to the end of the cache
        try:
            self.store[key] =self.store.pop(key)
            return self.store[key]
        except KeyError:
            if not hasattr(self, '__missing__'):
                raise
            else:
                return self.__missing__(key)
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __setitem__(self, key, value):
        try:
            self.store.pop(key)
        except KeyError:
            pass

        self.store[key] = value

        while len(self) > self.max_size:
            self.store.popitem(last=False)
    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)