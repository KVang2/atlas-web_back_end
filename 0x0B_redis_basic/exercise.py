#!/usr/bin/env python3
"""
Redis basic
"""

import redis


class Cache:
    def __init__(self):
        """
        store instance of Redis client as private
        variable named _redis using redis.Redis()
        flush instance using flushdb
        """
        # store instance of Redis client as private client
        self._redis = redis.Redis(host='localhost', port=6380, db=0)
        # flush redis database to start fresh
        self._redis.flushdb()

