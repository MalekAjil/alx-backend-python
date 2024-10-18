#!/usr/bin/env python3
"""Concurrent Coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return delays
