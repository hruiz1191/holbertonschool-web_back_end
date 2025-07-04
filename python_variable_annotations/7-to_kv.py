#!/usr/bin/env python3
"""
Module 7-to_kv
This module provides a function to return a tuple
with a string and a squared number.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of v as a float."""
    return (k, float(v ** 2))
