import asyncio


async def mygen(u: int = 10):
    """Yield powers of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)


async def main():
    '''asynchronous comprehension'''
    g = [x async for x in mygen()]
    f = [y async for y in mygen() if not (y//3 % 5)]
    return g, f


if __name__ == '__main__':
    g, f = asyncio.run(main())
    print(g)
    print(f)
