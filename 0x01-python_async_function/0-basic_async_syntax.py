#!/usr/bin/env python3
""" Basic Async Synatx"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive)
    and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay in seconds.
    """
    r: float = uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
