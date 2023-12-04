# input as flat text
a = {"Type": "A", "field1": "value1", "field2": "value2", "field3": "value3"}
b = "maçã"

print(b)
print(repr(b))

print(type(b))
print(type(repr(b)))

numbers = [1, 2, 3, 4]
print(numbers)
print(repr(numbers))

with open("./file.txt", "r") as file:
    print(repr(file.read()))

