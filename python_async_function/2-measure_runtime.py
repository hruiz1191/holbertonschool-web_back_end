#!/usr/bin/env python3
"""A file that measures the runtime of an async function"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures total runtime of wait_n(n, max_delay) and returns average time per call"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()


    total_time = end - start
    return total_time / n
