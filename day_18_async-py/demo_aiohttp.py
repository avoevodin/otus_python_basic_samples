import asyncio
from dataclasses import dataclass
from typing import Optional

import aiohttp
from loguru import logger


async def demo_query_httpbin():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/get") as resp:
            print(resp.status)
            print(await resp.text())
            print(await resp.json())


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
    Service(name="ip-shop", url="http://ip-api.com/json", field="query"),
]


async def fetch_ip(service: Service) -> Optional[str]:
    logger.info("fetch ip from {!r}", service.name)

    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as response:
            data: dict = await response.json()
            logger.info(
                "got response from {!r} with status {} and data {}",
                service.name,
                response.status,
                data,
            )
            return data.get(service.field)


async def get_my_ip(timeout: float = 0.5) -> str:
    logger.info("Searching for ip")
    tasks = {
        asyncio.create_task(fetch_ip(service), name=service.name)
        for service in SERVICES
    }
    coro = asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED, timeout=timeout)

    done, pending = await coro
    for task in pending:  # type: asyncio.Task
        task.cancel()
        logger.info("Cancelled task {}", task)

    my_ip = ""
    for task in done:
        my_ip = task.result()
        break
    else:
        logger.warning("Could not fetch IP!")

    logger.info("Finishing with IP {!r}", my_ip)
    return my_ip


if __name__ == "__main__":
    # asyncio.run(demo_query_httpbin())
    # asyncio.run(fetch_ip(SERVICES[0]))
    # asyncio.run(fetch_ip(SERVICES[1]))
    ip = asyncio.run(get_my_ip())
    ip1 = asyncio.run(get_my_ip(0.102))
    logger.info("done, ip {!r}", ip)
