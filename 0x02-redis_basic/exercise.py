#!/usr/bin/env python3
'''
    File exercise
'''
import redis
import uuid
from typing import Union


class Cache:
    """
        class for cache
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Method store
        """
        key = str(uuid.uuid4())
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
        else:
            raise TypeError("Data type not supported")
        return key

    def get(self,
            key: str,
            fn: callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """
            get method for cache
        """
        value = self._redis.get(key)
        if key is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self):
        """
            get method for cache
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self):
        """
            get method for cache
        """
        return self.get(key, fn=int)
