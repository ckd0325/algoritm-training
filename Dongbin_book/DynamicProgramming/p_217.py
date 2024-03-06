# 팁: 필요한 값만 저장하는게 아니라 가능한 모든 경우의 수를 다 저장해야 한다고 생각해야 풀이가 쉽다.

def answer():
    x = int(input())

    d = [0] * 30001
    start = 1

    for i in range(2, x + 1):

        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)

        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)

        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    print(d[x])