#!/usr/bin/env python3
"""A file that contains an asynchronous function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A function that waits for a random amount of time up to max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
