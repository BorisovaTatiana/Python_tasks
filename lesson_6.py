
# Задание_1

x = int(input("Введите число: "))

if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# Задание_2

x = int(input("Введите число: "))

if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

# Задание_3

x = input("Введите число: ")

if x in [1, 10]:
    print("Число в диапазоне")
else:
    print("Число вне диапазона")

# Задание_4

a = input("Введите первое число a: ")
b = input("Введите второе число b: ")

if a < b:
    a, b = b, a
    print(f"a = {a}, b = {b}")
else:
    nums = [a, b]
    nums.sort(reverse=True)
    print(nums)

# Задание_5

a = input("Введите первое число a: ")
b = input("Введите второе число b: ")

if a < b:
    print(f"Наименьшее число {a}")
else:
    print(f"Наименьшее число {b}")

# Задание_6

marks = [3, 4, 5, 2, 5, 4]

if 2 in marks:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")

# Задание_7

x = int(input("Введите число: "))

if x % 3 == 0 and x % 5 == 0:
    print("Число делится на 3 и 5")
elif x % 3 == 0:
    print("Число делится только на 3")
elif x % 5 == 0:
    print("Число делится только на 5")
else:
    print("Число не делится на 3 и 5")

# Задание_8

password = input("Введите пароль: ")

# 1 способ
if password == "admin123":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# 2 способ
if "admin123" in password:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# Задание_9

amount = float(input("Укажите сумму покупки: "))

if amount >= 5000:
    discount = 10
elif amount >= 1000:
    discount = 5
else:
    discount = 0

final_amount = amount * (100 - discount) / 100

print(f"Скидка: {discount}")
print(f"Итоговая цена: {final_amount}")

# Задание_10

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

mark = int(input("Введите оценку от 1 до 5: "))

# Задание_11

if mark == 5:
    print("Отлично!")
elif mark == 4:
    print("Хорошо")
elif mark == 3:
    print("Удовлетворительно")
elif mark == 1 or mark == 2:
    print("Неудовлетворительно")
else:
    print("Некорректная оценка")

# Задание_12

hours = int(input("Какое сейчас время суток? (укажите текущее время в часах от 0 до 23): "))

if hours < 0 or hours > 23:
    print("Некорректное время")
elif 6 <= hours <= 11:
    print("Утро")
elif 12 <= hours <= 17:
    print("День")
elif 18 <= hours <= 21:
    print("Вечер")
else:
    print("Ночь")

# Задание_13

temp = int(input("Укажите температуру на улице сейчас: "))
if temp < -10:
    print("Очень холодно")
elif -10 <= temp <= 0:
    print("Холодно")
elif 1 <= temp <= 10:
    print("Прохладно")
elif 11 <= temp <= 25:
    print("Тепло")
else:
    print("Жарко")

# Задание_14
#  = задача 10
years = int(input("Введите год: "))

if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

# Задание_15

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Укажите желаемую операцию (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"Результат сложения: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Результат деления: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Результат умножения: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Результат деления: {result}")
    else:
        print("Ошибка! По правилам математике: на ноль делить нельзя!")
else:
    print("Некорректно указана операция!")

# Задание_16

number = int(input("Введи любое число: "))
result = "четное" if number % 2 == 0 else "нечетное"
print(result)

# Задание_17

num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))

max_num = num_1 if num_1 > num_2 else num_2
print(max_num)

# Задание_18

number_1 = int(input("Введите любок целое число: "))

check_number_1 = "положительное" if number_1 > 0 else "отрицательное" if number_1 < 0 else "ноль"
print(check_number_1)

 # Задание_19

age = int(input("Введите свой возраст: "))
enter_age = "Вход разрешен" if age >= 18 else "Вход запрещен"
print(enter_age)

 # Задание_20

sum1 = float(input("Введите сумму покупки: "))
final_sum = sum1 * 0.9 if sum1 > 5000 else sum1
print(final_sum)


a = int(input("Введи свой балл: "))

if a > 90 and a <= 100:
    print("Excellent!")
elif a > 80 and a < 90:
    print("Good!")
elif a > 70 and a < 80:
    print("Bad!")
else:
    print("VERY BAD!")
