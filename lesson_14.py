# Задание_1

from math import sqrt, pow

print(sqrt(64))
print(pow(5, 3))


# Задание_2

import random

rand_num = random.randint(1, 10)
print(rand_num)
lang = ["Python", "Java", "C++"]
case_num = random.choice(lang)
print(case_num)


# Задание_3

import my_module

print(my_module.NAME)
print(my_module.add(3, 5))
print(my_module.multiply(4, 6))

# Задание_4

# main.py
from utils import greet
greet("Алексей")  # Привет, Алексей!

# Задание_5

import time
start = time.time()
time.sleep(2)
end = time.time()
duration = end - start
print(duration)
#  2.0050480365753174 - мой ответ

# Задание_6

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Должно вывести 200 - вывело



# Задание_7

# 7. Установите библиотеку matplotlib и постройте график.
# Напишите код:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 8. Создайте requirements.txt с зависимостями вашего проекта.
# Удалите один из установленных модулей, например requests
# Восстановите зависимости с помощью установки из requirements.txt

# Получилось, но не с первого раза =(

# 9. Создание простого пакета
# Создайте пакет math_operations с модулями:
# addition.py → Функция add(a, b) складывает 2 числа
# subtraction.py → Функция subtract(a, b) вычитает
# Структура проекта:
#
# math_operations/
# │── __init__.py
# │── addition.py
# │── subtraction.py
# main.py
#
# И запустите обе функции в main.py


# main.py (конечный вариант)
from math_operations import addition
from package import package_2

from utils import greet
greet("Алексей")

import package

package.package_1()
package.package_2()

print(package.NAME)

import math_operations

math_operations.addition(4, 6)
math_operations.subtraction(4, 6)

print(math_operations.addition(4, 6))
print(math_operations.subtraction(4, 6))
print(math_operations.NAME)



