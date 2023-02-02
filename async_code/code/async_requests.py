import aiohttp
import asyncio
from async_code import async_time_it


@async_time_it
async def get_async_request() -> list[dict]:
    """
    Выполнение асинхронных запросов
    """
    url = 'http://httpbin.org/delay/3'

    async with aiohttp.ClientSession() as session:
        res = await asyncio.gather(*[
            asyncio.create_task(session.get(url)) for i in range(5)
        ])

    result = [await i.json() for i in res]

    return result
