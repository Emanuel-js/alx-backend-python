#!/usr/bin/env python3
'''This module contains a sum_mixed_list function'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Takes a list with different datatypes and returns sum'''
    total = 0
    for num in mxd_lst:
        total = total + num
    return total
