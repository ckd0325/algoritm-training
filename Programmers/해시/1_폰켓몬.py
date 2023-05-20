# https://school.programmers.co.kr/learn/courses/30/lessons/1845

"""
풀이 포인트

nums에서 중복되지 않은 요소만 있는 리스트를 만듦
그 리스트의 길이가 뽑을 수 있는 몬스터 종류보다 작으면 리스트의 길이가 답이 될 것이고
아니라면 뽑을 수 있는 몬스터의 수가 답이 된다
"""
def solution1(nums):
    count = len(nums) // 2
    arr = []

    for num in nums:
        if num not in arr:
            arr.append(num)

    return min(count, len(arr))


