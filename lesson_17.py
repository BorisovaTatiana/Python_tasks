# Задание_1

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
result = list(filter(lambda x: isinstance(x, (str, list)), items))
print(result)

# Задание_2

def describe_type(x):
    if isinstance(x, bool):
        print("Это булево значение")
    elif isinstance(x, str):
        print("Это строка")
    elif isinstance(x, (int, float)):
        print("Это число")
    else:
        print("Неизвестный тип")

describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])


# Задание_3

def filter_list(f, data: list[int]) -> list[int]:
    return [item for item in data if f(item)]

nums = [1, 3, 5, 7]
print(filter_list(lambda x: x > 3, nums))  # [5, 7]

# Задание_4

def print_info(name: str, age: int, tags: list[str]) -> None:
    print(name, age, tags)

print_info("Tatiana", 36, ["программирование", "Python", "Москва"])

# Задание_5
# 5. Создай функцию def analyze(data),
# которая выводит количество элементов и среднее значение, если список не пустой.
# ===============================================
# ++++++++++++++++++++++++++++++++++++++++++++++++

def analyze(data):
    count = len(data)
    print(f"Количество элементов: {count}")
    if count > 0:
        average = sum(data) / count
        print(f"Среднее значение: {average}")
    else:
        print("Список пуст, среднее значение не вычисляется")

analyze([10, 20, 30, 40, 50])
analyze([])

# Задание_6

flags = [True, True, True, False]
all_true = all(flags)
print(all_true)
any_true = any(flags)
print(any_true)

# Задание_7

field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
first_row = field[0:3]
x_wins = all(cell == 'x' for cell in first_row)
print(x_wins)

# Задание_8

P = ['0', '0', '0', '*', '0']
mine = any(cell == '*' for cell in P)
print(mine)


# Задание_9

import random
colors = ["red", "green", "blue", "yellow", "purple"]
random_color = random.choice(colors)
print(f"Выбран цвет: {random_color}")

# Задание_10

random.seed(42)
numbers = [random.randint(0, 100) for _ in range(10)]
print(numbers)

# Задание_11

def greet(name: str) -> str:
    return f"Привет, {name}!"
result = greet("Татьяна")
print(result)

# Задание_12

def multiply(a: int | float, b: int | float) -> int | float:
    return a * b
result = multiply(4, 5)
print(result)

# Задание_13

def area(length: float, width: float) -> float:
    return length * width
print(area.__annotations__)