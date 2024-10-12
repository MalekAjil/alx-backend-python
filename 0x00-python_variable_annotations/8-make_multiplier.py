#!/usr/bin/env python3
"""Make Multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier."""
    def func(value: float) -> float:
        return value * multiplier
    return func
