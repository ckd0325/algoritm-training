# https://school.programmers.co.kr/learn/courses/30/lessons/42576

"""
풀이 포인트

리스트의 삭제는 O(n)의 복잡도이므로 해당 문제에서는 시간초과 발생
해시 자료구조를 사용하는 딕셔너리를 사용해보자
{"선수 이름": "해당 이름을 가지는 선수 수"}의 구조를 가지는 딕셔너리를 생성
이후 completion을 순회하며 value가 1인 경우에는 해당 요소 제거하고 아니면 value에 1을 빼준다
최후에는 {"완주하지 못한 선수이름":1} 요소만 남게된다.
"""
def solution(participant, completion):
    d = {}

    for p in participant:
        d[p] = 1 if p not in d else d[p] + 1

    for c in completion:
        if d[c] == 1:
            del d[c]
        else:
            d[c] -= 1

    return list(d.keys())[0]