import sys

inteiros = map(int,
               ['1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1',
                '2', '3', '4', '5'])

inteiros_2 = map(lambda x: x ** 2, inteiros)

inteiros_3 = range(10000)

inteiros_4 = list(range(100))

print(sys.getsizeof(inteiros))
print(inteiros)
for inteiro in inteiros_2:
    print(inteiro)

print(sys.getsizeof(inteiros))
print(sys.getsizeof(inteiros_2))
print(sys.getsizeof(inteiros_3))
print(sys.getsizeof(inteiros_4))  # Realize the difference to store in memory

'''
The key part of Lazy Evaluation is the generators
'''
def lazy_loading(items):
    for i in items:
        yield i


test_items = ['1', '2', '3', '4']
for i in lazy_loading(test_items):
    print(i)
