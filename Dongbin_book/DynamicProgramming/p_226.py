# 팁: 모든 화폐 단위를 한 번의 순회에 다 처리하지 않아도 된다. 한 단위씩 메모이제이션을 적용해보자

def answer():
    n, m = map(int, input().split())
    array = []
    for i in range(n):
        array.append(int(input()))

    d = [10001] * (m + 1)
    d[0] = 0

    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001:
                d[j] = min(d[j], d[j - array[i]] + 1)

    result = -1 if d[m] == 10001 else d[m]

    print(result)