import matplotlib.pyplot as plt
import time
y = []
for i in [100000 * j for j in range(10, 200)]:
    lst = list(range(i))
    t0 = time.time()
    x = lst.reverse()
    t1 = time.time()
    y.append(t1-t0)
plt.plot(y)
plt.xlabel("List elements (10**5)")
plt.ylabel("Time (sec)")
plt.show()
