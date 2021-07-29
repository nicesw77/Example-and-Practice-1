""" 함수의 미분2

도함수의 오차와 검증
"""
import numpy as np
import matplotlib.pyplot as plt

# 데이터 간격 h
h = 1.0


def f(x):
    return np.sin(x)


def g(func, xmin, xmax, h=0.01):
    x = np.arange(xmin, xmax, h)
    y = []
    y0 = func(xmin)
    for _x in x:
        y0 += func(_x + h) - func(_x)
        y.append(y0)
    return x, np.array(y)


if __name__ == "__main__":
    x = np.linspace(0, np.pi * 10, 100)
    plt.plot(x, f(x), "k--")
    plt.plot(*g(f, 0, np.pi * 10, h), "r")
    plt.grid(True)
    plt.show()
