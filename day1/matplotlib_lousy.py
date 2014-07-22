import matplotlib.pylab as plt
import random

xs = range(10)
ys1 = range(10)
ys2 = [random.randint(0,20) for i in range(10)]

fig = plt.figure(figsize=(10,5))

plt.plot(xs, ys1, label="line 1")
plt.plot(xs, ys2, label="line 2")

plt.legend(loc='upper center', ncol=4)

plt.savefig('twoline.png', format='png')


