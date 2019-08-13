"""
Expiring in-memory cache module
Geo Distributed LRU cache with time expiration & cleanup after timeout

Latency: one of the main factor which I took consideration,
        Usage of HashMap will help with greater extend, Since Addition & deletion takes O(n) time complexity and
        retrieval is much faster with O(1) complexity.

Design & Architecture:
1. The Source code is very simple this can be easily integrated for future enhancement.
2. This design holds good even in network failure or sudden crashes.
3. Current Writes are in real time. By creating API to access data across Geolocation, this can be more near real time.
4. Data consistency achieved by assigning timestamp to the individual data.
5. Locality of reference, I took it as Nearest locality to me(i.e India)
6. Flexible Schema
7. Cache can expire after certain time drift, also individual data can expire after the threshold time.

See more info on: https://github.com/prajwal041/ProblemSolving/blob/master/vanhack/Ormuco/LRU_cache_documentation
"""

import logging
import threading
from time import time,sleep
from collections import OrderedDict

__all__ = ['CachedObject', 'CacheInventory', 'CacheException']


class CacheException(Exception):
      """
      Generic cache exception
      """
      pass

class CachedObject(object):
    def __init__(self, name, obj, ttl):
        """
        Initializes a new cached object

        Args:
            name               (str): Human readable name for the cached entry
            obj               (type): Object to be cached
            ttl                (int): The TTL in seconds for the cached object

        """
        self.hits = 0
        self.name = name
        self.obj = obj
        self.ttl = ttl
        self.timestamp = time()

class CacheInventory(object):
    """
    Inventory for cached objects

    """
    def __init__(self, maxsize=0, housekeeping=0):
        """
        Initializes a new cache inventory

        Args:
            maxsize      (int): Upperbound limit on the number of items
                                that will be stored in the cache inventory
            housekeeping (int): Time in minutes to perform periodic
                                cache housekeeping

        """
        if maxsize < 0:
            raise CacheException('Cache inventory size cannot be negative')

        if housekeeping < 0:
                raise CacheException('Cache housekeeping period cannot be negative')

        self._cache = OrderedDict()
        self.maxsize = maxsize
        self.housekeeping = housekeeping * 60.0
        self.lock = threading.RLock()

        if self.housekeeping > 0:
            threading.Timer(self.housekeeping, self.housekeeper).start()

    def __len__(self):
        with self.lock:
            return len(self._cache)

    def __contains__(self, key):
        with self.lock:
            if key not in self._cache:
                return False

            item = self._cache[key]
            return not self._has_expired(item)

    def _has_expired(self, item):
        """
        Checks if a cached item has expired and removes it if needed

        If the upperbound limit has been reached then the last item
        is being removed from the inventory.

        Args:
            item (CachedObject): A cached object to lookup

        """
        with self.lock:
            if time() > item.timestamp + item.ttl:
                logging.debug(
                    'Object %s has expired and will be removed from cache [hits %d]',
                    item.name,
                    item.hits
                )
                self._cache.pop(item.name)
                return True
            return False

    def add(self, obj):
        """
        Add an item to the cache inventory

        Args:
            obj (CachedObject): A CachedObject instance to be added

        Raises:
            CacheException

        """
        if not isinstance(obj, CachedObject):
            raise Exception('Need a CachedObject instance to add in the cache')

        with self.lock:
            if 0 < self.maxsize == len(self._cache):
                popped = self._cache.popitem(last=False)
                print('Cache maxsize reached, removing ',popped,' [hits ',obj.hits,']')

            print('Caching object ', obj.name ,' ttl:',obj.ttl)
            self._cache[obj.name] = obj

    def get(self, key):
        """
        Retrieve an object from the cache inventory

        Args:
            key (str): Name of the cache item to retrieve

        Returns:
            The cached object if found, None otherwise

        """
        with self.lock:
            if key not in self._cache:
                return None

            item = self._cache[key]
            if self._has_expired(item):
                return None

            item.hits += 1
            print('Returning object', item.name, 'from cache [hits ',item.hits,']')
            return item.obj

    def schedule_housekeeper(self):
        """
        Schedules the next run of the housekeeper
        """
        if self.housekeeping > 0:
            t = threading.Timer(
                interval=self.housekeeping,
                function=self.housekeeper
            )
            t.setDaemon(True)
            t.start()

    def housekeeper(self):
        """
        Remove expired entries from the cache on regular basis
        """

        with self.lock:
            expired = 0
            print('Starting cache housekeeper [',len(self._cache),' items in cache]')
            print(self._cache)
            items =  list(self._cache.values())
            for item in items:
                if self._has_expired(item):
                    expired += 1
            print('Cache housekeeper completed [',expired,' removed from cache]')
            print("After cache : ", self._cache)
            # if self.housekeeping > 0:
            #     threading.Timer(self.housekeeping, self.housekeeper).start()
            self.schedule_housekeeper()
# maxsize=3
maxsize = int(input("Enter the maximum size of the cache: "))
housekeeping = int(input("Enter the time after the cache needs to be cleaned up(in Minutes): "))
# housekeeping=1
l = CacheInventory(maxsize,housekeeping)
while True:
    print('add')
    print('get')
    print('cleanup')
    print('quit')
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'add':
        name = str(input("Enter the values to add in the cache "))
        type = input("Enter the data type of the value ")
        if type == 'int':
            type = int(type)
        ttl = int(input("Enter the time expiration of the value in Seconds"))
        l.add(CachedObject(name=name,obj=type,ttl=ttl))
    elif operation == 'get':
        val = input("Enter the value to be retrieved")
        l.get(val)
    elif operation == 'cleanup':
        l.housekeeper()
    elif operation == 'quit':
         break
# l.add(CachedObject(name='A',obj=str,ttl=0))
# l.get('A')
# l.add(CachedObject(name='B',obj=str,ttl=0))
# l.add(CachedObject(name='C',obj=str,ttl=0))
# l.add(CachedObject(name='E',obj=str,ttl=0))
# l.add(CachedObject(name='F',obj=str,ttl=0))
# l.add(CachedObject(name='G',obj=str,ttl=0))
# l.add(CachedObject(name='H',obj=str,ttl=0))
# l.add(CachedObject(name='I',obj=str,ttl=0))
# l.add(CachedObject(name='J',obj=str,ttl=0))
# l.add(CachedObject(name='K',obj=str,ttl=0))
# l.add(CachedObject(name='L',obj=str,ttl=0))
# l.add(CachedObject(name='M',obj=str,ttl=0))
# l.add(CachedObject(name='N',obj=str,ttl=0))
# l.add(CachedObject(name='O',obj=str,ttl=0))
# l.add(CachedObject(name='P',obj=str,ttl=0))
# l.add(CachedObject(name='Q',obj=str,ttl=0))
# l.add(CachedObject(name='R',obj=str,ttl=0))
# l.add(CachedObject(name='S',obj=str,ttl=0))
# l.add(CachedObject(name='T',obj=str,ttl=0))
# l.add(CachedObject(name='U',obj=str,ttl=0))
# l.add(CachedObject(name='V',obj=str,ttl=0))
# l.add(CachedObject(name='W',obj=str,ttl=0))
# l.add(CachedObject(name='X',obj=str,ttl=0))
# l.add(CachedObject(name='Y',obj=str,ttl=1))
# l.add(CachedObject(name='Z',obj=str,ttl=120))
# l.add(CachedObject(name='1',obj=int,ttl=180))
#
# l.housekeeper()


# l.get('A')





