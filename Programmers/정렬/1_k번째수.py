# https://school.programmers.co.kr/learn/courses/30/lessons/42748

"""
풀이 포인트: 인덱스는 0부터 시작함을 유의
"""
def solution(array, commands):
    answer = []

    for comm in commands:
        slice = sorted(array[comm[0] - 1:comm[1]])
        answer.append(slice[comm[2] - 1])

    return answer
