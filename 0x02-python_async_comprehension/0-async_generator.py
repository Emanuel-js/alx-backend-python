#!/usr/bin/env python3
"""Python async comprehension"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """returns list"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
