"""몬티 홀 문제
"""
import matplotlib.pyplot as plt
import numpy as np

count = 1000  # 시행 수
doors = ["A", "B", "C"]  # 문


def monty_hall(count, doors, has_change=True):
    player = np.zeros(count)
    for idx in range(count):
        car = np.random.choice(doors)
        # 첫 번째 선택
        choice = np.random.choice(doors)

        # 사회자가 염소를 보여줌
        goats = doors.copy()
        goats.remove(car)
        try:
            goats.remove(choice)
        except:
            pass
        show = np.random.choice(goats)
        selection = doors.copy()
        selection.remove(show)

        # 선택을 변경할지 말지 결정
        if has_change:
            selection.remove(choice)
            last = np.random.choice(selection)
        else:
            last = choice
        print(
            f'{idx: 4d} Show [{"Success" if last == car else " Failed"}]: '
            f'choice "{choice}", Show goat "{show}", Car in "{car}"'
        )
        player[idx] = 1 if last == car else 0
    return player


def success_rate(play):
    rate = np.zeros(play.shape)
    for idx in range(play.shape[0]):
        cars = np.sum(play[: idx + 1])
        rate[idx] = cars / (idx + 1)
    return rate


if __name__ == "__main__":
    play_a = monty_hall(count, doors)  # 선택을 바꾸는 참가자
    play_b = monty_hall(count, doors, False)  # 선택을 바꾸지 않는 참가자
    plt.plot(range(count), success_rate(play_a), label="Change Selection")
    plt.plot(range(count), success_rate(play_b), label="Do not Change")
    plt.xlim(0, count)
    plt.ylim(0, 1)
    plt.xlabel("Cumulative number of Events")
    plt.ylabel("Cumulative Probability")
    plt.grid(True)
    plt.legend()
    plt.show()