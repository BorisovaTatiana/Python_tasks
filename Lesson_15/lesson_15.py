# Задание_1
from os.path import getsize

file_1 = "data.txt"
file_2 = "../requirments.txt"
f = open(file=file_1)
# text_1 = f.read()
# print(text_1)

# Задание_2

# text_1_line = f.readline()
# print(text_1_line)

# Задание_3

text_1_10 = f.read(10)
print(text_1_10)

# Задание_4
#
# 4. Прочитайте все строки файла и сохраните их в список. Затем выведите этот список.
# Ожидаемый вывод:
# ['Python – это мощный язык программирования.\n', 'Работа с файлами важна для автоматизации.\n', 'Чтение файлов в Python удобно и просто.\n']
# ===============================================

# Задание_5

with open(file_1) as f:
    for line in f:
        print(line.strip())

# Задание_6

with open(file=file_1) as f1:
    first_read = f1.read(5)
    print(first_read)

    f1.seek(0)

    second_read = f1.read(5)
    print(second_read)

# # Задание_7

size_file = getsize(file_1)
print(size_file)
print(f"Файл 'data.txt' имеет размер {size_file} байт")

# Задание_8

with open(file_1) as f3:
    content = f3.read()
    print(content)

f.close()

# Задание_9

try:
    f4 = open(file_1)
    print("Файл открыт")
    try:
        text = f4.read()
        print(text)
    finally:
        f4.close()
        print("Файл закрыт")

except FileNotFoundError:
    print("Файл не найден")


# Задание_10

#  Ответ задания 9?

# Задание_11

try:
    with open(file_1) as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# Задание_12
# 12. Создайте файл numbers.txt, который содержит по одному числу в каждой строке.
# Напишите программу, которая читает файл, суммирует все числа и выводит их сумму.
# Если файл не найден, программа должна вывести "Ошибка: Файл не найден".

try:
    with open('numbers.txt') as file_sum:
        total = sum(int(line.strip()) for line in file_sum)
    print(f"Сумма всех чисел: {total}")
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# Задание_13

from datetime import datetime

try:
    with open('log.txt', 'a') as f5:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        f5.write(f"{timestamp}\n")
    print(f"Запись добавлена: {timestamp}")

except Exception as e:
    print(f"Произошла ошибка: {e}")