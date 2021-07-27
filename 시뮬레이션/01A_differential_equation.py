import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 3 * x - np.cos(x)


def df(x):
    return 3 + np.sin(x)


def newton_method(x0, f, df):
    return x0 - (f(x0) / df(x0))


if __name__ == "__main__":
    x = np.linspace(0, 0.8)
    solution_0 = 1
    solution_x = []
    solution_y = np.linspace(0.5, 1.5, 5)
    for _ in solution_y:
        solution_0 = newton_method(solution_0, f, df)
        solution_x.append(solution_0)
    plt.plot(solution_x, solution_y, "ko", label="Newton method")
    plt.plot(x, 3 * x, label="$3x$")
    plt.plot(x, np.cos(x), label="$\cos x$")
    plt.grid(True)
    plt.legend()
    plt.show()