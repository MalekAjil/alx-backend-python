#!/usr/bin/env python3
"""To KV Module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments and returns tuple"""
    return (k, v ** 2)
