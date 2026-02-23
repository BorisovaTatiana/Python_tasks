
# Задание 1
name = "Tatiana"
age = 36
height = 1.59
print("Привет! Меня зовут ", name, "! Мне ", age, "лет и мой рост ", height)

# Задание 2
x = 10
print(x)
x = 25.5
print(x)
x = 'Python'
print(x)


# Задание 3

a = 7
b = a
print(a)
print(b)
a = 10
print(b) #потому что значение b после не было изменено


# Задание 4
x = y = z = 100
print(x, y, z)
print(id(x), id(y), id(z))

x = 150
y = 200
z = 250
print(x, y, z)
print(id(x), id(y), id(z))
#не очень поняла, зачем нужны id

# Задание 5
a = 5
b = 10
a, b = b, a
print(a)
print(b)


# Задание 6
import keyword
print(keyword.kwlist)


# Задание 7
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))



# Задание 8
name = "Tatiana"
age = 36
height = 1.59
weather = True
temperature = -15

print(name, age, height, weather, temperature)
print(type(name))
print(type(age))
print(type(height))
print(type(weather))
print(type(temperature))

переменная = 10
print(переменная)
# работает, но так делать не следует