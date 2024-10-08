#!/usr/bin/env python3
"""
Redis basic
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    single parameter named method,
    callable and returns a callable
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        key = method.__qualname__

        input_key = f"{key}:inputs"
        output_key = f"{key}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output

    return wrapper

def count_calls(method: Callable) -> Callable:
    """
    Arg: Callable
    returns: Callable
    create/return function that incre
    count for key everytime method is call
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        first arg
        """
        # method's qualified name as key store method call count
        key = method.__qualname__

        # increment count for key in redis
        self._redis.incr(key)

        # call original method and return result
        return method(self, *args, **kwargs)

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

    @call_history
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

def replay(cache: Cache, func: Callable):
    """
    display history of called particular
    function
    using lrange and zip to loop over
    inputs and outputs
    """
    key = func.__qualname__

    inputs_key = f"{key}:inputs"
    outputs_key = f"{key}:outputs"

    # Fetch all inputs/outputs from Redis
    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)


    for input_v, output_v in zip(inputs, outputs):
        print(f"{key}(*({input_v.decode('utf-8')},)) -> {output_v.decode('utf-8')}")
