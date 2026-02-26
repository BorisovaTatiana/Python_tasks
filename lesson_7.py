# Задание 1

n = int(input("Введите целое число: "))
i = 1

while i <= n:
    print(i)
    i += 1

# Задание 2

i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print(sum)

# Задание 3

num = int(input("Введите натуральное число: "))
count = 0
temp = num

while temp > 0:
    temp //= 10
    count += 1

print(count)

# Задание 4

num1 = int(input("Введите натуральное число: "))
max_num = 0
temp = num1

while temp > 0:
    n1 = temp % 10
    if n1 > max_num:
        max_num = n1
    temp //= 10

print(max_num)

# Задание 5

password_ok = "qwerty123"
password = ""

while password != password_ok:
    password = input("Введите пароль: ")
    if password != password_ok:
        print("Неверный пароль, попробуйте снова.")

print("Доступ разрешен!")

# Задание 6

numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(f"Четное число: {numbers[i]}")
        break
    i += 1
else:
    print("Четное число не найдено.")
# ИЛИ ЧЕРЕЗ ФЛАГ?

# Задание 7

total = 0

while True:
    num = int(input("Введите число(0 = выход): "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)

# Задание 8

a = int(input("Введите a: "))
b = int(input("Введите b: "))

i = a
while i <= b:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end = " ")
    i += 1

# Задание 9

N = int(input("Введите число N: "))

if N < 2:
    print("Не простое число")
else:
    i = 2
    while i <= N ** 0.5:
        if N % i == 0:
            print(f"Не простое число, так как делится на {i}")
            break
        i += 1
    else:
        print("Простое число")

# Задание 10

max_num = True

while True:
    num = input("Введите число ( 0 = выход): ")
    if num == "":
        print("Пользователь отказался вводить данные")
        break

    num_1 = int(num)
    if num_1 == 0:
        break

    if max_num is None or num_1 > max_num:
        max_num = num_1

if max_num is not None:
    print(f"Наибольшее число: {max_num}")
else:
    print("Числа не введены")

# Задание 11

text = input("Введите строку: ")
for char in text[::-1]:
    print(char, end="")

print()

# Задание 12
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0

print(numbers)

# Задание 13

N = int(input("Введите N: "))
power = []
for i in range(N + 1):
    power.append(2 ** i)

print(power)

# Задание 14

A = int(input("Введите А: "))
B = int(input("Введите B: "))
K = int(input("Введите K: "))

for i in range(A, B + 1, K):
    print(i, end="")