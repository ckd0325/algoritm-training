# https://school.programmers.co.kr/learn/courses/30/lessons/42626

"""
풀이 포인트:

음식을 섞어서 나온 스코빌 지수가 K 이상이라 해서 끝난게 아니다.
현재 음식에서 3번째로 안매운 음식이 K보다 작을 수도 있기 때문이다.
그러므로 힙에 Mix를 삽입한 뒤 루트 값이 K 이상인지 검증하는 과정이 필요
"""

import heapq


def solution(scoville, K):
    answer = 0
    arr_len = len(scoville)
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return 0

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1

    return answer
