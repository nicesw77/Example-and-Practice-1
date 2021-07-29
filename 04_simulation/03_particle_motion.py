import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

h = 0.01
time = np.arange(0, 1, h)

# 각 입자의 초기 위치와 초기 속도
position = [
    np.random.rand(2) * 2,
    np.random.rand(2) * 2,
    np.random.rand(2) * 2,
    np.random.rand(2) * 2,
    np.random.rand(2) * 2,
]
velocity = [
    (np.random.rand(2) * 2) - 1,
    (np.random.rand(2) * 2) - 1,
    (np.random.rand(2) * 2) - 1,
    (np.random.rand(2) * 2) - 1,
    (np.random.rand(2) * 2) - 1,
]
mass = [
    1.0,
    1.5,
    1.0,
    0.5,
    1.2,
]


def verlet_x(x, v, a):
    """위치 점화식"""
    dx = v * h + 0.5 * a * h ** 2
    return x + dx


def verlet_v(v, a):
    """속도 점화식"""
    dv = a * h
    return v + dv


def acceleration(xy1, xy2, m2):
    """중력을 계산하고 가속도로 출력"""
    r_sq = (xy2[0] - xy1[0]) ** 2 + (xy2[1] - xy1[1]) ** 2
    theta = np.arctan2(xy2[1] - xy1[1], xy2[0] - xy1[0])
    force = m2 / r_sq
    return np.array([force * np.cos(theta), force * np.sin(theta)])


def particle_motion(time, pos=[], vel=[], mass=[]):
    """벌렛 방법으로 입자의 궤도 작성"""
    pos_arr, vel_arr = [], []
    # 위치와 속도 배열 초기화
    for _pos, _vel in zip(pos, vel):
        vel_arr.append(np.zeros([time.shape[0], 2]))
        pos_arr.append(np.zeros([time.shape[0], 2]))
        pos_arr[-1][0, :] = _pos
        vel_arr[-1][0, :] = _vel
    # 운동 배열 채우기
    for idx in range(1, time.shape[0]):
        for num, pos, vel in zip(range(len(pos_arr)), pos_arr, vel_arr):
            acc0 = np.zeros(2)
            for pidx in [i for i in range(len(pos_arr)) if i != num]:
                m2 = mass[pidx]
                xy1 = pos[idx - 1]
                xy2 = pos_arr[pidx][idx - 1]
                acc0 += acceleration(xy1, xy2, m2)
            pos[idx, :] = verlet_x(pos[idx - 1], vel[idx - 1], acc0)
            acc1 = np.zeros(2)
            for pidx in [i for i in range(len(pos_arr)) if i != num]:
                m2 = mass[pidx]
                xy1 = pos[idx]
                xy2 = pos_arr[pidx][idx]
                acc1 += acceleration(xy1, xy2, m2)
            vel[idx, :] = verlet_v(vel[idx - 1], (acc0 + acc1) / 2)
    return pos_arr


if __name__ == "__main__":
    # 마커 크기: 운동을 진행할 수록 커지게
    size = np.linspace(1, 10, time.shape[0])
    # 색상표: 입자별로 색상을 고정
    color = list(mcolors.TABLEAU_COLORS)
    particles = particle_motion(time, position, velocity, mass)
    plt.figure(figsize=(5, 5))
    for plot, c in zip(particles, color):
        for idx, s in enumerate(size):
            plt.plot(plot[idx, 0], plot[idx, 1], ".", ms=s, color=c)
    plt.grid(True)
    plt.savefig("particle_dynamics_1.png", bbox_inches="tight")
