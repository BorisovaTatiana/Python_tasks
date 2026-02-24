
# Задание_1

cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [7, "apple", True, 6.7]

# Задание_2

print(cities[0])
print(numbers[-1])
# print(cities[10]) - IndexError: list index out of range

# Задание_3

numbers[1] = 10
mixed[-1] = "Python"

print(numbers)
print(mixed)

# Задание_4

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# Задание_5

list_1 = [1, 2, 3]
list_2 = [4, 5]

all_list = list_1 + list_2
print(all_list)

list_3 = ["Python", "is", "awesome"]
print(list_3 * 3)

# Задание_6

print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)

# Задание_7

del numbers[2]
print(numbers)
del cities[-1]
print(cities)

# Задание_8

str1 = "Python"
new_str1 = list(str1)
print(new_str1)
print(max(new_str1))
print(min(new_str1))
# print(sum(new_str1)) - type error

# Задание_9

towns_1 = ["Moscow", "St. Petersburg", "Kaluga", "Volokolamsk", "Moscow"]
towns_2 = towns_1[:]
print(towns_2)
print(towns_1 == towns_2)

# Задание_10

print(towns_1[1:3])
print(towns_1[2::])
# Выведи первые три элемента.
# Выведи весь список через срез.
# Используй отрицательные индексы для выбора последних двух элементов.
# print(towns_1[::4]) NO
# print(towns_1[::])
# print(towns_1[-2::]) yes

# Задание_11

print(towns_1[::2])
print(towns_1[::-1])
print(towns_1[::-2])


# Задание_12

towns_1 = ["Moscow", "St. Petersburg", "Sochi", "Kaluga", "Volokolamsk", "Moscow"]
towns_1[1:3] = ["Sochi", "Nizhniy Novgorod"]
print(towns_1)

towns_2 = ["Moscow", "St. Petersburg", "Sochi", "Kaluga", "Volokolamsk", "Moscow"]
# towns_2[::2] = ["Town"] * len(towns_2[::2]) выводится 1-3-5...
print(towns_2)

towns_3 = ["Moscow", "Volgograd", "Sochi", "Kaluga", "Volokolamsk", "Moscow"]
towns_3[1:3] = "Volgograd", "Omsk"
print(towns_3)

# Задание_13

list1 = [1, 2, 3]
list2 = [4, 5, 6]

all_lists = list1 + list2
print(all_lists)

str_list = ["Python", "rocks"]
print(str_list * 2)

# Задание_14

num_list1 = [1, 2, 3]
num_list2 = [1, 2, 3]

print(num_list1 == num_list2)

# Задание_15

chars = list("Python")
print(max(chars))
print(min(chars))
print(chars[0] + chars[1] + chars[2] + chars[3] + chars[4] + chars[5])
# символы объединились

# Задание_16
#
numbers = [5, 10, 15]
print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(1, 7)
print(numbers)
numbers.append("Python")
print(numbers)

# Задание_17

numbers.remove(10)
print(numbers)
#  Вопрос: почему 166 и 167 работают, а print(numbers.remove(10) не работает?
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)

# Задание_18

letters = ["a", "b", "c"]
copy_letters1 = letters.copy()
print(copy_letters1)
copy_letters2 = list(letters)
print(copy_letters2)
print(letters == copy_letters1 == copy_letters2)

# Задание_19

marks = [2, 3, 5, 3, 4, 5, 2, 3]
count_number = marks.count(3)
print(count_number)
index_number = marks.index(5)
print(index_number)
condition_number = 6 in marks
print(condition_number)

# Задание_20

nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)
nums.reverse()
print(nums)

# Задание_21

cities = ["Москва", "Тверь", "Вологда", "Санкт_Петербург", "Анапа", "Брест"]
print(cities)
cities.sort()
new_cities = sorted(cities)
print(cities)
print(new_cities)

# Задание_22

chars = list("programming")
print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort()
print(chars)
#  они выстроятся в алфавитном порядке

# Задание_23

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matrix)
print(matrix[1])
print(matrix[2][0])

# Задание_24

matrix[0] = [0, 0, 0, 0]
print(matrix)

matrix[1][3] = "Python"
print(matrix)

