#!/usr/bin/env python3
"""
Module 9-element_length
This module defines a function that returns the length of iterable elements.
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with elements and their lengths."""
    return [(i, len(i)) for i in lst]
