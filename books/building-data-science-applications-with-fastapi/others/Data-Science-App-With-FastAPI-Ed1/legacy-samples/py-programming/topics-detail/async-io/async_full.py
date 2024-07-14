# web-scraping URL collector App
import asyncio
import logging
import re
import aiohttp
import aiofiles

import urllib.error
import urllib.parse
import sys

from typing import IO
from aiohttp import ClientSession   # this is crawler

logging.basicConfig(    # logging configuration
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__file__)
logging.getLogger("chardet.charsetprober").disabled = True  # ??? chardet

HREF_RE = re.compile(r'href="(.*?)"')   # ???

# print("Hello Async")


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    ''' GET request wrapper to fetch page HTML
    kwargs are passed to `session.request()`
    '''
    resp = await session.request(method="GET", url=url, **kwargs)
    resp.raise_for_status()     # returns an HTTPError object if an error has occurred

    logger.info(f"Response status {resp.status} for url: {url}")

    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    """Find HREFs in the HTML of `url`."""
    found = set()

    try:
        html = await fetch_html(url, session=session, **kwargs)

    except (aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as e:
        logger.error(
            f"aiohttp exception for {url} [{getattr(e, 'status', None)}]: {getattr(e, 'message', None)}")
        return found

    except Exception as e:
        logger.exception(
            f"Non-aiohttp exception occured:  {getattr(e, '__dict__', {})}")
        return found

    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (url.error.URLError, ValueError) as e:
                logger.exception(
                    f"Error parsing {link}: {getattr(e, '__dict__', {})}")
            else:
                found.add(abslink)
        logger.info(f"Found {len(found)} links for {url}")
        return found


async def write_one(file: IO, url: str, **kwargs) -> None:
    """Write the found HREFs from `url` to `file`."""
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info(f"Wrote results for source URL: {url}")


async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    """Crawl & write concurrently to `file` for multiple `urls`."""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent
    # '''
    with open(here.joinpath('data', "urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath('data', "foundurls_3.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))
    # '''


message = """async IO program extend diractions:
    - recirsive crawling
    - aio-redis
    - networkx link connections
    - limit how many concurrent rqeuests are made in one batch
        by using asyncio semaphore objects:
            https://www.artificialworlds.net/blog/2017/05/31/python-3-large-numbers-of-tasks-with-limited-concurrency/
    
"""
