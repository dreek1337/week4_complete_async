import asyncpg
import asyncio
from async_code import async_time_it


@async_time_it
async def insert_values() -> None:
    """
    Асинхронная вставка в базу данных
    """
    async with asyncpg.create_pool(
        user='weather',
        password='danil1337danil',
        database='postgres',
        host='localhost',
        port=5432,
        min_size=50,
        max_size=50,
    ) as conn:
        async with asyncio.TaskGroup() as tg:
            for i in range(10):
                tg.create_task(conn.execute(
                    'INSERT INTO test_async_table (value_1, value_2) VALUES (1, 2)'
                ))
