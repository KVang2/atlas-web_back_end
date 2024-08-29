#!/usr/bin/env python3
"""
an asynchronous coroutine takes an int argument with
default value and waits for a random delay and returns it
"""


import asyncio
import random


def wait_random(max_delay: int = 10) -> float:
    """
    waiting for a random delay
    Args:
        10 (int):

    Returns:
        int:
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
