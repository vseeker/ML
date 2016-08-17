# coding=utf8
import numpy as np
import matplotlib.pyplot as plt

# original data
x = [x for x in xrange(1, 10)]
print x
y = [0.199, 0.399, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]
A = np.vstack([x, np.ones(len(x))]).T
print A

# 调用最小二乘法函数
a, b = np.linalg.lstsq(A, y)[0]

# 转化为numpy array
x = np.array(x)
y = np.array(y)

# show it
plt.plot(x, y, 'o', label='Oringinal data', markersize=10)
plt.plot(x, a * x + b, 'r', label='Fited line')
plt.show()

