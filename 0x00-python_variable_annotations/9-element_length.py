#!/usr/bin/env python3
"""Element Length"""
from typing import Tuple, Sequence, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list of tuple of sequence"""
    return [(i, len(i)) for i in lst]
