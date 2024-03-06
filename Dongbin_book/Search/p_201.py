# 팁: 이진 탐색을 활용해야 시간제한 안걸림
# 내 방법은 간단해보이지만 효율적이지 못함

def my_answer():
    n, m = map(int, input().split())
    rc = list(map(int, input().split()))

    base = max(rc)

    for i in range(base, -1, -1):
        temp = []
        for j in range(n):
            result = 0 if rc[j] - i < 0 else rc[j] - i
            temp.append(result)

        length = sum(temp)
        if m <= length:
            print(i)
            break

def book_answer():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    start = 0
    end = max(array)

    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)