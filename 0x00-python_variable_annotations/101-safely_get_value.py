#!/usr/bin/env python3
"""Safely Get Value"""
from typing import Union, Any, Mapping, NewType, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """more involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
