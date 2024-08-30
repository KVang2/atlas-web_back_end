#!/usr/bin/env python3
"""
a measure time function with int n,
max_delay that measures total execution time
"""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measure total execution time and returns a float
    Args:
        n (int): execution time
        max_delay (int): delay time

    Returns:
        float: returing total time / n
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
