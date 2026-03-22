# Задание_1

str_1 = ["Python", 123, "Java", 456, "C++", 789]
str_gen = filter(lambda x: isinstance(x, str), str_1)
print(*str_gen)

int_gen = filter(lambda x: isinstance(x, int), str_1)
print(*int_gen)

# Задание_2

import random

random_gen = [random.randint(1, 100) for _ in range(10)]
print(f"Все числа: {random_gen}")
print(f"Максимальное число: {max(random_gen)}")

# Задание_3

with open('words.txt', 'w') as f6:
    f6.write("apple banana cat elephant python")

def words_gen(filename, min_length=5):
    with open(filename, 'r') as f7:
        for line in f7:
            for word in line.split():
                if len(word) > min_length:
                    yield word

print(*words_gen('words.txt'))

# Задание_4

with open('text.txt', 'w') as f8:
    f8.write("""
Hello world
Python is great
I love coding in Python
Java is also good""")

with open('text.txt', 'r') as f8:
    for line in (l.strip() for l in f8 if 'Python' in l):
        print(line)

# Задание_5
#
# import random
# gen = (random.randint(1, 100) for _ in iter(int, 1))  # бесконечный генератор
# for num in gen:
#     print(num, end=' ')
#     if num == 50:
#         break

# Задание_6

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

print(*prime_generator(10))

# Задание_7
# 7. Создайте функцию-генератор, которая имитирует загрузку данных из API.
# Генератор должен возвращать строки "Получены данные 1", "Получены данные 2", …
# Остановите генерацию после 5 вызовов next().
# Ожидаемый вывод:
# Получены данные 1
# Получены данные 2
# Получены данные 3
# Получены данные 4
# Получены данные 5
# ===============================================

def make_gen():
    for i in range(1, 6):
        yield f"Получены данные {i}"

gen = make_gen()
for _ in range(5):
    print(next(gen))

# Задание_8

user_input = input("Введите числа через пробел: ")
squares = list(map(lambda x: int(x) ** 2, user_input.split()))
print(f"Квадраты чисел: {squares}")

# Задание_9

cities = ["Москва", "Санкт-Петербург", "Казань"]
upper_cities = list(map(str.upper, cities))
print(upper_cities)

# Задание_10

numbers = [15, 30, 45, 22, 60, 77, 90, 100]
result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(result)

# Задание_11
# 11. Используя filter(), получите из списка только строки, содержащие хотя бы одну цифру.
# Дан список: ["hello", "world42", "python3", "abc", "123", "data1science"].

strings = ["hello", "world42", "python3", "abc", "123", "data1science"]
result = list(filter(lambda s: any(c.isdigit() for c in s), strings))
print(result)

# Задание_12

countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
result = dict(zip(countries, capitals))
print(result)

# Задание_13
# 13. Используйте zip(*iterable), чтобы выполнить обратное преобразование списка кортежей:
# data = [(1, 'a'), (2, 'b'), (3, 'c')]
# Распакуйте его в два отдельных списка:
# [1, 2, 3]
# ['a', 'b', 'c']

data = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*data)
print(list(numbers))
print(list(letters))

# Задание_14

names = ["петр", "Иван", "мария", "Анна"]
sorted_names = sorted(names, key=lambda x: not x[0].isupper())
print(sorted_names)

# Задание_15

products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)