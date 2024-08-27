#!/usr/bin/env python3
"""
script that conatins async generator function
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An async generator yields a random number between 0 and 10

    yields:
       float: a number from 0 to 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
