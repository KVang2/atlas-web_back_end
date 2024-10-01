#!/usr/bin/env python3
"""
Redis basic
"""

import redis
import uuid
from typing import Union, Callable


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
