

# Imperative Programming
nome = "BRUNO"
lista = []

for l in nome:
    lista.append(l)

print(lista)

# Functional Programming
func_name = lambda x: x
lista = list(map(str, func_name('BRUNO')))
print(lista)


numbers = [10, 15, 21, 33, 42, 55]

mapped_numbers = list(map(lambda x: x ** 2, numbers))
print(mapped_numbers)


# Functional Programming
lista = list(map(lambda x: x+'a', nome))
print(lista)