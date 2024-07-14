import aiohttp
import asyncio
import time


async def download_site(session, url):
    # notify the event loop that it’s blocked???
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        for res in asyncio.as_completed(tasks):
            await res
        # await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()

    # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    asyncio.run(download_all_sites(sites))  # alternative to run_until_complete

    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
