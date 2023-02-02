from time import time


def time_it(func):
    def inner(*args, **kwargs):
        start_time = time()

        complete_function = func(*args, **kwargs)

        result_time_test = round(time() - start_time, 1)

        print(result_time_test)

        return complete_function

    return inner
