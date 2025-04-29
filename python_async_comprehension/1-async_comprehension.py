#!/usr/bin/env python3
import asyncio
import time

async def measure_runtime():
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time
