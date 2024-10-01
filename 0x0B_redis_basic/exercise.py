#!/usr/bin/env python3
"""
Redis basic
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """
    Arg: Callable
    returns: Callable
    create/return function that incre
    count for key everytime method is call
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        first arg
        """
        key = func.__qualname__

        self._redis.incr(key)

        current_count = self._redis.get(key).decode('utf-8')
        return func(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        """
        store instance of Redis client as private
        variable named _redis using redis.Redis()
        flush instance using flushdb
        """
        # store instance of Redis client as private client
        self._redis = redis.Redis(host='localhost', port=6379, db=0)

        # flush redis database to start fresh
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes data arg and returns string
        generate random key using uuid
        """
        # r_key to generate random key
        r_key = str(uuid.uuid4())

        # store data
        self._redis.set(r_key, data)
        return r_key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, None]:
        """
        retrieve data
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        get str, parametrize Cache.get
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        get str, parametrize Cache.get
        with correct conversion function
        """
        return self.get(key, lambda x: int(x))

    def replay(self):
        """
        display history of called particular
        function
        using lrange and zip to loop over
        inputs and outputs
        """
        return None
    