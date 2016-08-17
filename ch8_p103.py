# coding=utf8
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# original data
T = [x for x in xrange(1960, 1969)]
print T
S = [29.72, 30.61, 31.51, 32.13, 32.34, 32.85, 33.56, 34.20, 34.83]
xdata = np.array(T)
ydata = np.log(np.array(S))


def func(x, a, b):
    return a + b * x

# 使用非线性最小二乘法拟合函数
popt, pcov = curve_fit(func, xdata, ydata)
print '*', popt
print "#", pcov
# show it
# plt.plot(xdata, ydata, 'ko', label='Original Noised data')
# plt.plot(xdata, func(xdata, *popt), 'r', label='Fitted Curve')
# plt.show()

