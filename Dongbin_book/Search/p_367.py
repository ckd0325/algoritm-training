from bisect import bisect_left, bisect_right

def my_answer():
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = arr[bisect_left(arr, x):bisect_right(arr, x)]

    if len(ans) == 0:
        print(-1)
    else:
        print(len(ans))

def count_by_value(array, x):

    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않을 경우
    if a == None:
        return 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수를 반환
    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간값의 값 보다 찾고자 하는 것이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    # 중간값의 값 보다 찾고자 하는 것이 큰 경우 왼쪽 확인
    else:
        return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른에 있는 경우에만 인덱스 반환
    if (mid == len(array)-1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간값의 값 보다 찾고자 하는 것이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    # 중간값의 값 보다 찾고자 하는 것이 크거나 같은 경우 왼쪽 확인
    else:
        return last(array, target, mid+1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 x인 데이터의 수 계산
count = count_by_value(array, x)

# 값이 x인 원소가 존재하지 않은다면
if count == 0:
    print(-1)
else:
    print(count)

