# coding=utf8
import numpy as np
import matplotlib.pyplot as plt

# original data
x = [x for x in xrange(1, 10)]
y = [0.199, 0.399, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]
t1 = t2 = t3 = t4 = 0
n = len(x)
for i in xrange(n):
    t1 += y[i]
    t2 += x[i]
    t3 += x[i] * y[i]
    t4 += x[i] ** 2
a = (t1*t2/n - t3) / (t2*t2/n - t4)
b = (t1 - a*t2) / n

# 转化为numpy array
x = np.array(x)
y = np.array(y)

# show it
plt.plot(x, y, 'o', label='Oringinal data', markersize=10)
plt.plot(x, a * x + b, 'r', label='Fited line')
plt.show()

