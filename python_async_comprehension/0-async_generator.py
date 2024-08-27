#!/usr/bin/env python3
"""
script that conatins async generator function
"""


import asynico
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None];
    """
    An async generator yields a random number between 0 and 10

    yields:
        a number from 1 to 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
