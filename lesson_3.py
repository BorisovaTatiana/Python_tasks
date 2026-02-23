#
# # Задание 1
# print("Привет, мир!")
# print("5" + " " + "10" + " " + "15")
#
# # Задание 2
#
# print(1, 2, 3, sep=" & ")
# print("Python", end=" ")
# print("лучший язык")
#
# # Задание 3
#
# x = 3.14
# y = -8
# print(f"Координаты -  {x} и {y}")
#
# name = str(input("Как тебя зовут?"))
# age = int(input("Сколько тебе лет?"))
# answer = (f"Имя: {name}, возраст: {age}")
# print(answer)
#
# # Задание 4
#
# name1 = str(input("Как тебя зовут?"))
# print(f"Привет, {name1}")
#
#
# # Задание 5
#
# number1 = float(input("Введи первое число: "))
# number2 = float(input("Введи второе число: "))
# print("Сумма введеных чисел: ", number1 + number2)
# number3 = int(input("Введи еще одно число(целое): "))
# print("Квадрат этого числа: ", number3 ** 2)
#
#  # Задание 6
#
# print(5 > 3)
# print(10 < 2)
# print(7 == 7)
# print(6 != 8)
# print(4 >= 4)
# print(9 <= 3)
#
# res = 8 > 12
# print(res)
# print(type(res))
#
# # Задание 7
#
# x = 15
# if x % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")
#
# #Не знаю, как оформить
#
# if x % 5 == 0:
#     print("OK")
# else:
#     print("Not OK")
#
# if x % 3 == 0 and x % 5 == 0:
#     print("OK")
# else:
#     print("Not OK")
#
# # Задание 8
#
# y = 4.5
# print(y >= 1 and y <= 10)
# print((y in [0,5]) or (y in [1,10]))
# print(not y < 5)
#
# # Задание 9
#
# print(True or False and False)
# print(not False and True)
# print(False and True)
# print(not (10 > 5 or 3 < 1))
#
# # Задание 9
#
#
# print(bool(0))
# print(bool(-5))
# print(bool(3.14))
# print(bool(""))
# print(bool("Python"))
# print(bool(" "))
#
#
# # Доп. задание 1
#
# n = 7
# if n > 0 and n % 2 == 0 and n % 3 == 0:
#     print(f"n = {n} и совпадают все условия")
# else:
#     print("Не совпадает одно или более из условий")
#

# Доп. задание 2

s = "Программирование"
# print(s[0])
# print(s[-1])
# print(s[2] + " " + s[-2])

# Доп. задание 3
# print(s[100]) - IndexError: string index out of range
print(s[len(s)-1])


# Доп. задание 4

s = "Программирование"
print(s[:6])
print(s[-5:])
print(s[2:7])
print(s[::2])
print(s[::-1])


# Доп. задание 5

s = "Программирование"
print(s[::3])
print(s[::-2])

# Доп. задание 6

# s[0] = "п" - нужна заглавная буква
s2 = "П" + s[1::]
print(s2)

# Доп. задание 7

word = "abcdefgh"
new_word1 = word[2:5]
print(new_word1)

print(word[::-1])
print(word[1:-1])
