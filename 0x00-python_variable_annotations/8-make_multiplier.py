#!/usr/bin/env python3
'''This module contains an make_multiplier function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''takes a float and return a function'''
    def my_func(multiply: float) -> float:
        '''multiplies a float by a function'''
        return multiplier * multiply
    return my_func
