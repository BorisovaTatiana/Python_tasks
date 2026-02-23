
# Задание_1

s = "Python для автоматизации"
s1 = s.lower()
print(s1)
s2 = s.upper()
print(s2)


# Задание_2
msg = "абракадабра"
print(msg.count("ра"))

# Определи количество "а", начиная с 3-го символа. ИСПРАВИТЬ
print(msg.count("a"), 2)



# Задание_3
index_first = msg.find("ка")
print(index_first)

index_last = msg.rfind("а")
print(index_last)

surprise = msg.find("xyz")
print(surprise)
# ВЫВЕЛ -1


# Задание_4

text = "Я изучаю Java"
new_text = text.replace("Java", "Python")
print(new_text)

new_text2 = "".join(new_text.split())
print(new_text2)



# Задание_5
str1 = "Python"
print(str1.isalpha())

str2 = "12345"
print(str2.isdigit())

str3 = "123abc"
print(not str3.isdigit())


# Задание_6

code = "42"
new_code = code.zfill(7)
print(new_code)

str_1 = "text"
new_str = str_1.ljust(10, '*')
print(new_str)
# не уверена в последнем задании с выравниванием

# Задание_7

# Разбей строку "яблоко, груша, банан" на список слов.
# Разбей "Python;Java;C++" по ";". ИСПРАВИТЬ
fruits = "apple, pear, banana"
list_fruits = fruits.split(", ")
print(list_fruits)

languages = "Python; Java; C++"
list_languages = languages.split("; ")
print(list_languages)



# Задание_8

list = ["Привет", "мир", "!"]
new_str = " ".join(list)
print(new_str)

list2 = ["apple", "banana", "cherry"]
new_list2 = ", ".join(list2)
print(new_list2)


# Задание_9


str1 = " Python"
print(str1.lstrip())

str2 = "Python "
print(str2.rstrip())

str3 = " Python "
print(str3.strip())



# Задание_10

text = "программирование"
# first_letter = text[0].upper() ВЫВОДИТ ТОЛЬКО ПЕРВУЮ БУКВУ
first_letter = text.capitalize()
print(first_letter)

amount_letters = text.count("р")
print(amount_letters)

index = text.find("и")
print(index)

# Разверни строку и выведи результат.НЕ РАЗВЕРНУЛО!
# text_revers = text[::-1]
print(text)


# Задание_11

text = "Hello\nPython"
# \n - спецсимвол, который переносит на следующую строку
print(text)

# Задание_12
t = "Python\tAutomation"
# \t - спецсимвол, который имеет горизонтальную табуляцию
print(t)


# Задание_13

path = "C:\new\test.txt"
# print(path) - неправильно использованные обратные слэши
# и неправильное восприятие \n -- \t

path_new_1 = "C:\\new\\test.txt"
print(path_new_1)
path_new_2 = r"C:\new\test.txt"
print(path_new_2)

drink = "Марка вина \"Ягодка\""
print(drink)


# Задание_14
#
path = r"C:\new\test.txt"
print(path)

# Все символы "\"воспринимаются буквально,
# как обычные символы


# Задание_15

s = "Hello\b World"
print(s) # удалилась буква "o"

s = "Hello\fPython"
print(s) # переход на новую строку? но этого не произошло


# Задание_16

# Создай переменные имя и возраст.
# Сформируй строку "Меня зовут {имя}, мне {возраст} лет." с помощью оператора + и выведи её.
# Попробуй добавить число в строку без str(). Что произойдёт?
# ИСПРАВИТЬ!

name = "Tatiana"
age = 36
# result = "My name is " + name + " and my age is " + str(age)
# print(result)
# Этот вариант считаю правильным, но он у меня не выводится. Пишет ошибку, в чем проблема - не могу понять

# result_1 = "My name is " + name + " and my age is " + age
# print(result_1)


# Задание_17

result_2 = "Привет, меня зовут {} и мне {} лет".format(name, age)
print(result_2)
result_3 = "Привет, меня зовут {name} и мне {age} лет".format(name=name, age=age)
print(result_3)
result_wrong = "Привет, меня зовут {} и мне {} лет".format(age, name)
print(result_wrong)



# Задание_18

city = "Москва"
year = 2026

print(f"Сегодня {year} год, и я живу в {city}.")
print(f"Через 5лет будет {year + 5} год.")


# Задание_19

print(f"Дважды мой возраст : {age * 2}")
print(f"Мое имя в верхнем регистре: {name.upper()}")


# Задание_20

# Используя .format(), сформируй строку "Курс валют: 1 доллар = 92.5 рубля.", подставляя переменные.
# Используя F-строку, сформируй "Квадрат числа 7 равен 49.", вычисляя 7 ** 2 прямо внутри строки.
# МСПРАВИТЬ!!!
course = 92.5
print("Курс валют: ", format(course), "рубля")

number = 7
print(f"Квадрат числа {number} равен {number ** 2}")
