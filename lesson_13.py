# Задание_1

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world"

print(say_hello())

# Задание_2

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()


# Задание_3

def cache(func):
    cache_dict = {}
    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        result = func(*args)
        cache_dict[args] = result
        return result
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)

# Задание_4

import time

def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            all_time = 0
            for _ in range(repeat):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                all_time += end - start
            avg_time = all_time / repeat
            print(avg_time)
        return wrapper
    return decorator

@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
# у меня получилось 1.0037612120310466, а при 4 - 1.002141793568929