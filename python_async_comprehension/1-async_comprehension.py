#!/usr/bin/env python3
""" File that contains the function async comprehension """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers asynchronously using async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers between 0 and 10.
    """
    return [number async for number in async_generator()]
