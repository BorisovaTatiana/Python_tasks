
# Задание_1

set_1 = {1, 2, 3}
set_1.add(4)
set_1.add(2)
print(set_1)

# Задание_2

cities = ["Moscow", "Novgorod", "Tverj", "Kaluga", "St.Petersburg", "Moscow"]
print(cities)
uniq_city = set(cities)
print(uniq_city)


# Задание_3

numbers = set(range(1, 11))
print(numbers)
numbers.remove(5)
numbers.discard(15)
print(numbers)

# Задание_4

word = "abrakadabra"
chars_word = set(word)

print(chars_word)
print(len(chars_word))

# Задание_5

set_2 = set()
set_2.add(10)
set_2.add("hello")
set_2.add((1, 2, 3))
# set_2.add([4, 5, 6]) список изменяемый, а остальное нет
print(set_2)

# Задание_6

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)
print(A | B)
print(A - B)
print(B - A)
print(A ^ B)

# Задание_7

even_numbers = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}

print(even_numbers & odd_numbers)
# set()
print(even_numbers | odd_numbers)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Задание_8

python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}

print(python_students & java_students)
print(python_students ^ java_students)
print(java_students | python_students)

# Задание_9

text1 = set("программирование")
text2 = set("автоматизация")

print(text1 & text2)
print(text1 - text2)
print(text1 ^ text2)

# Задание_10

squares = {x ** 2 for x in range(1, 11) if x % 2 == 0}
print(squares)

# Задание_11

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
unique_words = {word.upper() for word in words}
print(unique_words)

# Задание_12

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
result = {name: "отлично" if score >= 80 else "удовлетворительно" for name, score in grades.items()}

print(result)

# Задание_13

text = {"Python", "automation", "programming", "testing"}
word_len = {word: len(word) for word in text}
print(word_len)

# # Задание_14

n = 10
result = {i: {j ** 2 for j in range(1, i + 1)} for i in range(1, n + 1)}
print(result)
