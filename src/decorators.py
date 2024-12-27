from datetime import time
from functools import wraps


def log(filename=None):
    """Декоратор для логирования функции, аргументов, результатов и ошибок"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error.__class__.__name__}.Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


def printing(func):
    """Фиксирует начало и конец работы функции """

    def wrapper(*args, **kwargs):
        print(f"Function {func} started")
        result = func(*args, **kwargs)
        print(f"Function {func} finished")
        return result

    return wrapper


def timer(func):
    """Фиксирует время, которое затратит функция на выполнение"""

    def wrapper(*args, **kwargs):
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        return result

    return wrapper


@printing
@timer
def my_function():
    for i in range(100000000):
        continue
