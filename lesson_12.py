# Задание_1
from lesson_2 import count

square = lambda x: x ** 2
print(square(5))
print(square(10))

# Задание_2

even_number = lambda x: x % 2 == 0
print(even_number(5))
print(even_number(10))

# Задание_3

words = ["pear", "banana", "apple", "cherry"]
sort_words = sorted(words, key = lambda x: x[-1])
print(sort_words)

# Задание_4

def multiply_by(n):
    return lambda x: x * n
times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))

# Задание_5

def counter(start = 0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c1 = counter(5)
c2 = counter()
print(c1())
print(c1())
print(c2())
print(c2())