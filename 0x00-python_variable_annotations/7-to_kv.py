#!/usr/bin/env python3
'''This module contains a to_kv function'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a string and multiplies the float by 2'''
    return(k, v ** 2)
