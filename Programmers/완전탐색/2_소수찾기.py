# https://school.programmers.co.kr/learn/courses/30/lessons/42839#

"""
풀이 포인트

n>1이 합성수이면 n은 p<=sqrt(n)인 소인수 p를 갖는다.
이를 이용하여 n이 소수인지 판별하는 함수를 만들 수 있다.
그리고 순열을 이용하여 해당 문자열로 만들 수 있는 모든 수를 한 리스트에 담고 중복을 제거한다.
해당 리스트를 순회하며 담겨있는 수가 소수인지 판별하면 된다.
"""

import math
from itertools import permutations, combinations


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0:
        return False
    else:
        for n in range(3, int(math.sqrt(num)) + 1, 2):
            if num % n == 0:
                return False
    return True


def solution(numbers):
    answer = 0
    all_nums = []

    for i in range(1, len(numbers) + 1):
        strs = list(permutations(numbers, i))
        nums = [int(''.join(s)) for s in strs]
        all_nums.extend(nums)

    all_nums = set(all_nums)
    for n in all_nums:
        if is_prime(n):
            print(n)
            answer += 1

    return answer