import asyncio


async def printer(name: str, times: int) -> None:
    for _ in range(times):
        print(name)
        print("========")
        await asyncio.sleep(0.5)


async def main():
    await asyncio.gather(
        printer("A", 3),
        printer("B", 3),
        printer("C", 4),
        printer("D", 5),
        printer("E", 6),
    )


asyncio.run(main())