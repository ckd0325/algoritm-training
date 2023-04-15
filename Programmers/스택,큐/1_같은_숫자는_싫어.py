# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

from collections import deque


def solution(arr):
    answer = []
    queue = deque(arr)
    answer.append(queue.popleft())
    while queue:
        num = queue.popleft()
        if answer[-1] != num:
            answer.append(num)

    return answer