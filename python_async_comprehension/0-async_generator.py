#!/usr/bin/env python3
""" File that contains the function async generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ An asynchronous generator that yields random floating point numbers """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
