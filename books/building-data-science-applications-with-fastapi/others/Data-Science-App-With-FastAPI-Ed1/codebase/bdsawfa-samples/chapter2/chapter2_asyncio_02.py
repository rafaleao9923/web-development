import asyncio


# asynchronous programming
async def main():
    print("Hello ...")
    # await keyword suspends execution of a coroutine until it completes and returns the result data
    await asyncio.sleep(1)
    print("... Hung!")


asyncio.run(main())