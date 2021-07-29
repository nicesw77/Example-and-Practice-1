"""몬테카를로를 이용한 파이값 근사

"""
import numpy as np
import matplotlib.pyplot as plt

count_lim = 8001

points = np.zeros([count_lim, 2])
calc_pi = np.zeros([count_lim, 2])
result_pi = 0.0
inner = 0
for count in range(count_lim):
    points[count, :] = pos = np.random.rand(2)
    if np.sum(pos ** 2) < 1:
        inner += 1
    result_pi = 4 * inner / (count + 1)
    calc_pi[count, :] = count + 1, result_pi
    if count % 100 == 0:
        print(f"Monte carlo progress: {count} / {count_lim}")

circle = np.linspace(0, np.pi)
pi_line = np.array([[0, count_lim], [np.pi, np.pi]])
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 3))
ax1.plot(*points.T, ".k", alpha=0.3)
ax1.plot(np.sin(circle), np.cos(circle), "r")
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)

ax2.plot(*calc_pi[:count].T, "k", alpha=0.3)
ax2.plot(*pi_line, "r--")
ax2.text(0, 1.5, f" Results of {count} trials:\n  {result_pi}")
ax2.grid(True)
ax2.set_ylim(0, 5)
ax2.set_xlim(0, count_lim)
plt.savefig(f"monte_carlo_{count:06d}.png", bbox_inches="tight")
# plt.show()
