

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# NUMBER = 3
# (lambda x: print(x**2))(NUMBER)


# Iterate over lista and get another list with quadratic numbers
quadratic = map(lambda x: x**2, lista)
print(id(quadratic))
quadratic_list = set(quadratic)
print(id(quadratic))
print(id(quadratic_list))
print(quadratic_list)
quadratic_set = list(quadratic_list)
print(id(quadratic))
print(id(quadratic_list))
print(id(quadratic_set))

print(quadratic)
print(quadratic_set)
