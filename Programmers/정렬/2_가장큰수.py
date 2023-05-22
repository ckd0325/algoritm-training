# https://school.programmers.co.kr/learn/courses/30/lessons/42746

"""
일단 모든 요소를 문자열로 변환.
numbers의 원소는 0~1000이니깐 numbers의 모든 요소를 *3하면 한자리 수도 세자리 수가 된다(str이지만)
이를 내림차순 정렬하면 문자열이므로 아스키코드 기준으로 정렬된다. 즉 이것들을 모두 이어붙여주면 답이 나온다.
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))
