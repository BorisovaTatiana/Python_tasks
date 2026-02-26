
# Задание_1

fruits_dict = {"apple": 169.99, "banana": 129.99, "orange": 68.99}
fruits_dict["pear"] = 239.99
print(fruits_dict)

# Задание_2

grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
students = [name for name, grade in grades.items() if grade >= 4]
print(students)

# Задание_3

countries = {"Russia": "Moscow", "France": "Paris", "Italy": "Rome"}
country = input("Введите страну: ")
capital = countries.get(country, "Страна не найдена")
print(capital)

# Задание_4

students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
courses = {}
for name, course in students:
    if course not in courses:
        courses[course] = []
    courses[course].append(name)
print(courses)

# Задание_5

grades = {"Anna": 5, "Boris": 4, "Alex": 3, "Jane": 2}
min_student = min(grades, key=grades.get)
grades.pop(min_student)
print(grades)
print(min_student)

# Задание_6

students = ["Анна", "Борис", "Виктор", "Галина"]
ages = dict.fromkeys(students, None)
ages["Анна"] = 20
ages["Борис"] = 22
ages["Виктор"] = 21
ages["Галина"] = 19
print(ages)

# Задание_7

exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
currency = input("Введите валюту (USD, EUR, GBP): ")
if currency in exchange_rates:
    print(exchange_rates[currency])
else:
    print("Неизвестная валюта")
    exchange_rates[currency] = None
    print(exchange_rates)

# Задание_8

dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)

# Задание_9

tuple_new= (12, "python", 3.14, True, [1,2,3])
print(tuple_new[1])
print(tuple_new[-1])

# Задание_10

nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
count_4 = nums.count(4)
print(count_4)
index_7 = nums.index(7)
print(index_7)

# Задание_11

lst = ["Python", "Java", "C++", "JavaScript"]
tpl = tuple(lst)
print(tpl)
print("C++" in tpl)

# Задание_12

numbers = tuple(range(1, 11))
print(numbers[:3])
print(numbers[-3:])
print(numbers[::2])

# Задание_13

tpl_1 = ([1, 2, 3], {"fruits": "apple"})
# нельзя изменить кортеж, можно только изменить список внутри него и словарь
tpl_1[0].append(4)
print(tpl_1)
tpl_1[1]["vegetables"] = "tomato"
print(tpl_1)