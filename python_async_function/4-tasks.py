#!/usr/bin/env python3
"""A file that executes task_wait_random n times concurrently"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns list of delays in order"""
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
