import requests
from sync_code import time_it


@time_it
def get_requests() -> list[dict]:
    """
    Выполнение запросов на сайт
    """
    url = 'http://httpbin.org/delay/3'

    result = []

    for _ in range(5):
        result.append(requests.get(url).json())

    return result


print(get_requests())
