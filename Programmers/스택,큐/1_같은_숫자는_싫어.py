# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

from collections import deque

"""
풀이 포인트

arr를 deque로 변환한다.
queue가 빌 때까지 popleft()를 하여 변수에 넣어준다.
해당 변수가 answer의 마지막 안덴스의 값과 같지 않다면 answer에 append() 해준다.
"""
def solution(arr):
    answer = []
    queue = deque(arr)
    answer.append(queue.popleft())
    while queue:
        num = queue.popleft()
        if answer[-1] != num:
            answer.append(num)

    return answer
