import asyncio
from async_code import get_async_request, insert_values


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(get_async_request())
        tg.create_task(insert_values())


if __name__ == '__main__':
    asyncio.run(main())
