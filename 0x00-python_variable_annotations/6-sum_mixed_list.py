#!/usr/bin/env python3
"""Sum Mixed List"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of list elements"""
    s: float = 0
    for x in mxd_lst:
        s += x
    return s
