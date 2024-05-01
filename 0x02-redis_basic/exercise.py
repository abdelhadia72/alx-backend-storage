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

    def count_calls(method: callable) -> callable:
        """
            count calls
        """
        key = method.__qualname__

        def wrapper(self, *args, **kwargs):
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache class methods to track call count
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Wraps called method and adds its call count redis before execution
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator for Cache class method to track args
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """ Wraps called method and tracks its passed argument by storing
            them to redis
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper
