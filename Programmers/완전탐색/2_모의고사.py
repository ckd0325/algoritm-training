# https://school.programmers.co.kr/learn/courses/30/lessons/42840

"""
풀이 포인트

a, b, c 각각 5/8/10 문제마다 정답 패턴이 반복됨을 인지한다.
answer 리스트의 인덱스와 값을 enumerate()를 이용해 순회하며 i번째 문제의 답을 맞췄는지 기록한다
가장 많은 문제를 맞춘 사람(들)만 뽑아낸다.
"""
def solution(answers):
    counts = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]

    for i, val in enumerate(answers):
        if val == a[i % 5]:
            count[0] += 1
        if val == b[i % 8]:
            count[1] += 1
        if val == c[i % 10]:
            count[2] += 1

    max_val = max(count)
    answer = [i + 1 for i, v in enumerate(count) if v == max_val]

    return answer
