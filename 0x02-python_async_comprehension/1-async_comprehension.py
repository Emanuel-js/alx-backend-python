#!/usr/bin/env python3
"""Python async comprehension"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """return azync list"""
    done_tasks = [i async for i in async_generator()]
    return done_tasks
