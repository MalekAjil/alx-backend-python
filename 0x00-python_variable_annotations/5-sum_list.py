#!/usr/bin/env python3
"""Sum List Module"""


def sum_list(input_list: [float]) -> float:
    """returns sum of list items"""
    s: float = 0
    for x in input_list:
        s += x
    return s
