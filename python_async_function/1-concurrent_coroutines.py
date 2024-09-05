#!/usr/bin/env python3
"""
an asynchronous coroutine takes an int argument with
default value and waits for a random delay and returns it
"""


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        List[float]: _description_
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays