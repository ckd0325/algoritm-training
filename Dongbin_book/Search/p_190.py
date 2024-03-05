# 이진 탐색
# 코테 단골 주제

def binary_search(arr, target, start, end):

    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)

arr = [1,2,3,4,5,6,7,8,9]

print(binary_search(arr, 4, 0, len(arr)-1))

