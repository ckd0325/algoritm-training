# 팁: 앞에서부터 길이 3인 경우부터 부분해를 구해나가면 된다.

def my_answer():
    n = int(input())
    k = list(map(int, input().split()))
    arr = [0] * n

    arr[0] = k[0]
    arr[1] = max(k[0], k[1])

    for i in range(2, n):
        arr[i] = max(arr[i - 2] + k[i], arr[i - 1])

    print(arr[n - 1])

def book_answer():
    n = int(input())

    array = list(map(int, input().split()))
    d = [0] * n

    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2]+array[i])

    print(d[n-1])
