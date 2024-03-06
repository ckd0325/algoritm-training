# 팁: 주어진 타일을 이용하면 i-2, i-1까지 타일이 채워진 이후의 경우의 수를 고려해 점화식을 세울 수 있다.

def answer():
    n = int(input())

    array = [0] * 1001

    array[1] = 1
    array[2] = 3

    for i in range(3, n + 1):
        array[i] = (array[i - 1] + array[i - 2] * 2) % 796796

    print(array[n])