# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    counts = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0, 0, 0]
    answer = [0, 0, 0]

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
