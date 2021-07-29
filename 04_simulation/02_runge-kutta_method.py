import numpy as np
import matplotlib.pyplot as plt


h = 0.1
x0 = 0
t0, t1 = 0, 10


def f(t, x):
    return np.sin(t)


def RK_method(func, x0, t0, t1, h=0.01):
    """룽게-쿠타 방법
    func: 함수(t, x)
    x0: x 초기값
    t0, t1, h: 시간의 시작값, 끝값, 간격
    """
    time = np.arange(t0, t1, h)
    x = np.zeros(time.shape)
    x[0] = x0
    for idx in range(1, x.shape[0]):
        k1 = func(time[idx - 1], x[idx - 1])
        k2 = func(time[idx - 1] + h / 2, x[idx - 1] + k1 / 2)
        k3 = func(time[idx - 1] + h / 2, x[idx - 1] + k2 / 2)
        k4 = func(time[idx - 1] + h, x[idx - 1] + k3)
        dx = (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
        x[idx] = x[idx - 1] + dx
    return time, x


if __name__ == "__main__":
    time, x = RK_method(f, x0, t0, t1, h)
    plt.plot(time, x)
    plt.show()