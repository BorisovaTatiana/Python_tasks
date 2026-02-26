# Задание 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator1 = iter(list1)
# while True:
#     print(next(iterator1))

# Задание_2
text = "Python"
iterator2 = iter(text)
# while True:
#     print(next(iterator2))

# Задание_3

N = int(input("Введите N: "))
squares = [x ** 2 for x in range(1, N + 1)]
print(squares)

# 2. Сформируйте список, содержащий только
# четные числа в диапазоне от -10 до 10.
# ===============================================

# Задание_4

numbers = [x for x in range(-10, 11) if x % 2 == 0]
print(numbers)

# Задание_5
words = ["Python", "PHP", "Swift", "C++"]
len_words = [len(word) for word in words]
print(words)
print(len_words)

# Задание_6
list_3 = ["четное" if x % 2 == 0 else "нечетное" for x in range(1, 21)]
print(list_3)

# 5. Проверка, является ли объект итерируемым
# Создайте список внутри которого 3 объекта: число, строка и список.
# Создайте генератор в котором будет написано True - если объект является итерируемым или False - если нет.
#
# Задание_7

# не понимаю, как сделать =(
lists_4 = [5, "python", [1, 2, 3]]