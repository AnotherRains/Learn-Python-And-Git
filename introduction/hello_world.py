# Just some operation
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# Test Strings
print("Ya Habibie")
print("Bie Family")
print("Indonesia")
print("I am enjoying 30 days of python")

# Check Data Types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Ya Habibie"))
print(type("Bie Family"))
print(type("Indonesia"))

# Exercise 1
print(type(4))
print(type(4.0))
print(type(4 + 4j))
print(type("Dayumn Bruh"))
print(type(True))
print(type([1, "2", 3.0, 4 + 4j]))
print(type((1, "2", 3.0, 4 + 4j)))
print(type({"name", "Bie", "age", 20}))
print(type({"name": "Bie", "age": 20}))

# Exercise 2
a, b = [x - y for x, y in zip((10, 8), (2, 3))]
c = (a**2 + b**2)**0.5
print(c)