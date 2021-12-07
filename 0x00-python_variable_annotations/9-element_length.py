#!/usr/bin/env python3
'''This module contains an element_length function'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a list of tuple that iterates'''
    return [(i, len(i)) for i in lst]
