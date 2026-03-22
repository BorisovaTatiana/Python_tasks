squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x ** 2 for x in range(10)]

print(squares)

numbers = [1, 2, 3, 4, 5, 6]

even = [x for x in numbers if x % 2 == 0]

print(even)

result = [x if x % 2 == 0 else "NO" for x in numbers]
print(result)

matrix = [[1, 2], [3, 4], [5, 6]]
list1 = [num for row in matrix for num in row]
print(list1)


