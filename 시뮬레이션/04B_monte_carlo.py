"""방사성 붕괴
"""
import matplotlib.pyplot as plt
import numpy as np

nuclides_n = 500  # 핵종의 수
probability = 0.01  # 단위시간당 붕괴 확률
time_max = 300  # 관측 시간


def decay_event(nuclides, probability):
    """붕괴 단일 이벤트"""
    func = lambda x: 1 if np.random.rand() > probability and x > 0 else 0
    return np.vectorize(func)(nuclides)


if __name__ == "__main__":
    nuclides = np.ones(nuclides_n)
    x = np.arange(time_max)
    y = []
    for i in x:
        y.append(np.sum(nuclides))
        nuclides = decay_event(nuclides, probability)
    plt.bar(x, y, 1, color="#AAA")
    plt.plot(x, nuclides_n * np.exp(-probability * x), "r--")
    plt.xlabel("Time")
    plt.ylabel("Number of nuclides")
    plt.xlim(0, time_max)
    plt.ylim(0, nuclides_n)
    plt.show()
