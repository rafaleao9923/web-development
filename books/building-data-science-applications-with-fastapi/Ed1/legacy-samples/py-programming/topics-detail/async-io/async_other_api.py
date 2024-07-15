# create_task
import asyncio
import time     # add more


async def coro(seq) -> list:
    """'IO' wait time is proportional to the max element."""
    await asyncio.sleep(max(seq))
    return list(reversed(seq))


async def main():
    '''
    # This is a bit redundant in the case of one task
    # We could use `await coro([3, 2, 1])` on its own
    t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
    await t
    print(f't: type {type(t)}')
    print(f't done: {t.done()}')
    '''

    t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
    t2 = asyncio.create_task(coro([10, 5, 0]))      # add more

    print('Start:', time.strftime('%X'))

    # a = await asyncio.gather(t, t2)     # chain???
    # another way to do it (can check which task complete):
    for res in asyncio.as_completed([t, t2]):
        compl = await res
        print(f'res: {compl} completed at {time.strftime("%X")}')

    print('End:', time.strftime('%X'))

    print(f'Both tasks done: {all((t.done(), t2.done()))}')

    # return a  # not need if we use `as_completed`


# t = asyncio.run(main())
a = asyncio.run(main())
