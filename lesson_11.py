# Задание_1

def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")
greet("Анна")

# Задание_2

def square(num):
    return num ** 2
print(square(5))

# Задание_3

def is_even(num):
    return num % 2 == 0
print(is_even(4))
print(is_even(7))

# Задание_4

def repeat_string(text, times):
    return text * times

print(repeat_string("Python", 3))

# Задание_5

def add(a, b):
    return a + b
print(add(3, 7))

# Задание_6

def get_max(a, b, c):
    return max(a, b, c)
print(get_max(10, 25, 7))

# Задание_7

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "На ноль делить нельзя!"
    else:
        return "Неизвестная операция"

print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))

# Задание_8

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

# Задание_9

def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_spaces:
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    return s1 == s2

print(compare_strings("Hello", " hello "))
print(compare_strings("Hello", "HELLO", ignore_case=False))
print(compare_strings("Hello ", "Hello", ignore_spaces=False))

# Задание_10

def summarize(*args):
    all_num = 0
    for item in args:
        if isinstance(item, (int, float)):
            all_num += item
    return all_num

print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))

# Задание_11

def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print("Дополнительная информация:")
    for key, value in extra.items():
        print(f"{key}: {value}")

create_profile("Иван", 30, city="Москва", job="Инженер")

# Задание_12

def process_orders(*orders, discount=0):
    total = sum(orders)
    discounted = total * (100 - discount) / 100
    print(f"Сумма заказа: {total}")
    print(f"С учетом скидки: {discounted}")
    return discounted

process_orders(100, 200, 300, discount=10)

# Задание_13

def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

print(merge_lists([1, 2], [3, 4], [5, 6]))

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))