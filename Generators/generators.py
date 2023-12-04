import string


def f():
    return 1


print(f())


# yield retorna um objetor Generator
# Since a generator is a type of iterator, we should be able do loop over this
def g():
    yield 1
    yield 2
    yield 3


print(g())

# Let's loop over the generator!
for i in g():
    print(i)


# We can generate the lowe case Ascii Letters
# Remember to import string
def letters():
    for c in string.ascii_lowercase:
        yield c


# Iterating over the generator (letters() function)
for i in letters():
    print(i)

'''
Therefore, a function that returns "yield" instead of "return" is called a generator function, or simply a generator

In C++, yield statements are used by threads to return control to another process

The generator function will return data until the generator has run out of yields

It is like a Ping Pong Game: the "for" over the "letters" function willl return the next character every iterator

'''


# Another example with vowels list:
def vowels_list():
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        yield vowel


for letter in vowels_list():
    print(letter)

