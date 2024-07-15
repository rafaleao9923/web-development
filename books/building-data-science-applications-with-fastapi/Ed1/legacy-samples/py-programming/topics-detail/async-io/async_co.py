import time
import asyncio
try:
    from collections.abc import Iterable  # noqa
except ImportError:
    from collections import Iterable  # noqa


async def stuff():
    print("one")
    await asyncio.sleep(1)
    print("two")


# def stuff_stuff():  # Error when await on a non async function
#     print("one")
#     time.sleep(1)
#     print("two")


@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff()
    # yield from stuff_stuff()


async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff()   # returns an iterator
    # await stuff_stuff()


def rountine_one():
    s = time.perf_counter()
    asyncio.run(py34_coro())
    elapsed = time.perf_counter() - s
    return f"{__file__} executed in {elapsed:0.2f} seconds."


def rountine_two():
    s = time.perf_counter()
    asyncio.run(py35_coro())
    elapsed = time.perf_counter() - s
    return f"{__file__} executed in {elapsed:0.2f} seconds."


if __name__ == "__main__":
    '''
    print(isinstance(py34_coro, Iterable))
    print(isinstance(py35_coro, Iterable))
    '''
    print(rountine_one())
    print(rountine_two())
