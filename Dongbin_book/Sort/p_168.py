# 퀵소트 함수 구현 예시

def quick_sort1(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 첫 번째 원소를 피벗으로 잡음
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽, 오른쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)


def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


array1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort1(array1, 0, len(array1) - 1)

array2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

print(array1)
print(quick_sort2(array2))
