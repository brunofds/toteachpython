

# There are three functions which facilitate a functional approach to programming.

'''
Map: Applies a function to all items in a input list (could be any iterable argument)
map(function_to_apply, list_of_inputs)
If we want to pass all the list elements to a function one-by-one add then collect the output
'''

# Simple and naive example
items = ['1', '2', '3', '4']
int_items = []

# How can we generate another list with the same values but as int fiels (not string)?
# int_items = int(items) ## It gerenates an error! It must be a string!
# print(int_items) TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

# Iterating over the list and turning items to int
for i in items:
    int_items.append(int(i))
print(items)
print(int_items)

'''
What about the complexity?
We have to iterate over all items once (linear growth), so we have the O(n) complexity
'''




