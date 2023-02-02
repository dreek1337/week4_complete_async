import psycopg2
from sync_code import time_it


@time_it
def insert_db() -> None:
    """
    Вставка в базу данных
    """
    with psycopg2.connect(
            user='weather',
            password='danil1337danil',
            database='postgres',
            host='localhost',
            port=5432
    ) as conn:
        with conn.cursor() as cur:
            for i in range(100):
                cur.execute(
                    f'INSERT INTO test_async_table (value_1, value_2) VALUES ({str(i)}, {str(i + i)})'
                )
                conn.commit()
