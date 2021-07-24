"""개미집단 최적화
"""
import matplotlib.pyplot as plt
import numpy as np

area = np.ones([20, 20])
start = (1, 1)
goal = (19, 14)

pheromone = 1.0
volatility = 0.3


def get_neighbors(x, y):
    """x, y와 이웃한 좌표 목록 출력"""
    max_x, max_y = area.shape
    return [
        (i, j)
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if (i != x or j != y) and (i >= 0 and j >= 0) and (i < max_x and j < max_y)
    ]


def ant_path_finding():
    path = [start]
    x, y = start
    count = 0
    while x != goal[0] or y != goal[1]:
        count += 1
        if count > 400:
            # print("Path Finding Fail")
            return None
        neighbors = get_neighbors(x, y)
        values = np.array([area[i, j] for i, j in neighbors])
        p = values / np.sum(values)
        x, y = neighbors[np.random.choice(len(neighbors), p=p)]
        while (x, y) == path[-1]:
            x, y = neighbors[np.random.choice(len(neighbors), p=p)]
        path.append((x, y))
    return path


def step_end(path):
    global area
    if path is None:
        return
    for x, y in set(path):
        area[x, y] += pheromone / len(set(path))
    area[:, :] = area * (1 - volatility)
    return


count = 0
while count < 40:
    path = ant_path_finding()
    if path is None:
        continue
    count += 1
    print(count)
    step_end(path)
    if count < 20:
        continue
    x, y = [], []
    for _x, _y in path:
        x.append(_x)
        y.append(_y)
    plt.plot(x, y, "b", alpha=0.3)
plt.imshow(area.T, cmap="Greens")
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.show()
