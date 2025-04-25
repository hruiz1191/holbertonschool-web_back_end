#!/usr/bin/env python3
"""A file that contains a wait"""

import asyncio
from typing import List

wR = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function that waits n times for random delays"""
    tasks = [asyncio.create_task(wR(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
