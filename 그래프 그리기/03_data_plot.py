"""파일의 데이터로 그래프 그리기

input.csv로부터 데이터를 읽어들여서 그래프로 출력
"""
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

"""
소스코드의 실행 디렉토리와 데이터파일의 디렉토리가 일치하도록 조정
"""

import matplotlib.pyplot as plt

x = []
y = []

with open("input.csv", "r") as f:
    for line in f.readlines():
        items = line.split(" ")
        x.append(float(items[0]))
        y.append(float(items[1]))

if __name__ == "__main__":
    plt.scatter(x, y)
    plt.xlim(0, 1)
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.savefig("data_plot_1.png", bbox_inches="tight")
    # plt.show()