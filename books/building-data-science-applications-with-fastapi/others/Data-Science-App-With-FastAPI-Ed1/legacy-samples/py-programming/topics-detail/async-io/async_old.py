# old-style generator-based coroutines
import asyncio
from itertools import cycle


@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine"""
    # No need to build these yourself, but be aware of what they are
    s = yield from stuff()
    return s


async def py35_coro():
    """Native coroutine, modern syntax"""
    s = await stuff()
    return s


async def stuff():
    return 0x10, 0x20, 0x30


def gen():
    yield 0x10, 0x20, 0x30


def endless():
    yield from cycle((9, 8, 7, 6))


def handle_endless():
    e = endless()
    total = 0
    for i in e:
        if total < 30:
            print(i, end=" ")
            total += i
        else:
            print()
            break
    # resume
    print(next(e), next(e), next(e))


if __name__ == "__main__":
    g = gen()
    print(g)    # generator
    print(next(g))  # iterates over the generator

    handle_endless()