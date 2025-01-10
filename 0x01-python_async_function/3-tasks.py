#!/usr/bin/env python3
"""Tasks Module"""

import asyncio
wait_random = __import__('0_basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for wait_random with the given max_delay."""
    return asyncio.create_task(wait_random(max_delay))