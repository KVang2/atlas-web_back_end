#!/usr/bin/env python3
"""
Function that takes int max delay and return asyncio task.
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay (int): integer

    Returns:
        int: asyncio.task
    """
    return asyncio.create_task(wait_random(max_delay))
