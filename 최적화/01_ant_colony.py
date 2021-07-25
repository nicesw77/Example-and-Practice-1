"""개미집단 최적화
"""
import matplotlib.pyplot as plt
import numpy as np

area = np.ones([20, 20])  # 지역 생성
start = (1, 1)  # 개미 출발지점
goal = (19, 14)  # 도착해야 하는 지점
path_count = 40  # 경로를 만들 개미 수
path_max_len = 20 * 20  # 최대 경로 길이

pheromone = 1.0  # 페로몬 가산치
volatility = 0.3  # 스탭 당 페로몬 휘발율


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
    """개미 경로 생성"""
    path = [start]
    x, y = start
    count = 0
    while x != goal[0] or y != goal[1]:
        count += 1
        if count > path_max_len:
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
    """경로를 따라 페로몬을 더하고 전 지역의 페로몬을 한번 휘발시킴"""
    global area
    if path is None:
        return
    for x, y in set(path):
        area[x, y] += pheromone / len(set(path))
    area[:, :] = area * (1 - volatility)
    return


if __name__ == "__main__":
    # 계산 및 그래프 작성
    count = 0
    while count < path_count:
        path = ant_path_finding()
        if path is None:
            continue
        count += 1
        print(f"Ant Pathfinding: {count} / {path_count}")
        step_end(path)

    # 최종 경로와 페로몬 맵 그리기
    x, y = [], []
    for _x, _y in path:
        x.append(_x)
        y.append(_y)
    plt.plot(x, y, "b", alpha=0.3)
    plt.imshow(area.T, cmap="Greens")
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.show()
