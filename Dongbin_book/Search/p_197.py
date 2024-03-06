# 팁: 내부 라이브리를 사용하면 간단

def my_answer():
    n = int(input())
    arr_n = list(map(int, input().split()))

    m = int(input())
    arr_m = list(map(int, input().split()))

    print(arr_n)
    print(arr_m)

    for i in arr_m:
        if i in arr_n:
            print("yes", end=" ")
        else:
            print("no", end=" ")

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
def book_answer_using_binary():
    n = int(input())
    array = set(map(int, input().split()))

    m = int(input())
    x = list(map(int, input().split()))

    for i in x:
        result = binary_search(array, i, 0, n - 1)
        if result is not None:
            print("yes", end=" ")
        else:
            print("no", end=" ")


def book_answer_using_set():
    n = int(input())
    array = set(map(int, input().split()))

    m = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if i in array:
            print("yes", end=" ")
        else:
            print("no", end=" ")