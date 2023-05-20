# https://school.programmers.co.kr/learn/courses/30/lessons/86491

"""
풀이 포인트

하나의 직사각형에서 긴 쪽은 무조건 가로, 짧은 쪽은 무조건 세로라는 식의 기준을 잡자
그렇게 하면 가로와 세로에서 가장 큰 값이 결국 정답이 된다.
"""
def solution(sizes):
    ans_ver = 0
    ans_hor = 0

    for size in sizes:
        ver = max(size[0], size[1])
        hor = min(size[0], size[1])

        ans_ver = ver if ans_ver < ver else ans_ver
        ans_hor = hor if ans_hor < hor else ans_hor

    return ans_ver * ans_hor