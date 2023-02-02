from time import time


def async_time_it(func):
    async def inner(*args, **kwargs):
        start_time = time()

        complete_function = await func(*args, **kwargs)

        result_time_test = round(time() - start_time, 1)

        print(result_time_test)

        return complete_function

    return inner
