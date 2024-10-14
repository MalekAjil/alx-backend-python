#!/usr/bin/env python3
""" Basic Async Synatx"""
import asyncio
from random import uniform


async def wait_random(max_delay: float = 10) -> float:
    """ waits for a random delay between 0 and max_delay
    seconds and eventually returns it."""
    r: float = uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
