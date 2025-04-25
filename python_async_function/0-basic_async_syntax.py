#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay and returns it."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay (inclusive) and return it.

    Args:
        max_delay (int): Maximum number of seconds to wait (default is 10).

    Returns:
        float: The actual number of seconds waited (random).
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
