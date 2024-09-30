#!/usr/bin/env python3
"""
Redis basic
"""

import redis
import uuid
from typing import Union


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
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key
