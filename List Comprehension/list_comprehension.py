# Using list comprehension as "for" alternative
# Advantage: Simple, clean and fast!
import time

price_list = [500, 1000, 1500, 2000, 2500, 3000, 3500]
new_price_list = []

# Case: Products with price greater than 1500, pay 50% tax (add the new prices in another list)

# Using fors
for price in price_list:
    if price > 1500:
        new_price_list.append(price * 2)
print(new_price_list)

# Using List Comprehension
new_price_list_2 = [price * 2 for price in price_list if price > 1500]
print(new_price_list_2)


# PS: Can we say that List Comprehension is faster than for loops? Probably yes!
iterations = 10000000

# For loop
start = time.time()
mylist = []
for i in range(iterations):
    mylist.append(i+1)
end = time.time()
print("Time for loop with list:", end - start)
print("Size list:", len(mylist))

# List Comprehension - Better time, but just because we are creating lists by appending new elements every iteration.
# This is slow
start = time.time()
mylist = [i+1 for i in range(iterations)]
end = time.time()
print("Time List Comprehension with list:", end - start)
print("Size list:", len(mylist))


# If we do not use list, probably for will be better in fast terms
# For loops
start = time.time()
for i in range(iterations):
    i+1
end = time.time()
print(end - start)

# List Comprehension (slower here)
start = time.time()
[i+1 for i in range(iterations)]
end = time.time()
print(end - start)


# We can create a list, with number range, using the range and iterations. Faster algorithm!
start = time.time()
mylist = list(range(iterations))
end = time.time()
print(end - start)
print("Time for list + range and interations:", end - start)
print("Size list:", len(mylist))







