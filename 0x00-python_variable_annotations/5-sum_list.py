#!/usr/bin/env python3
'''This module contains a sum_list function'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Takes a list as an argument and return the sum of the list'''
    total = 0
    for num in input_list:
        total = total + num
    return total
