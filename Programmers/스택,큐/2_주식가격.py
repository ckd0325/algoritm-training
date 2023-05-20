# https://school.programmers.co.kr/learn/courses/30/lessons/42584

"""
풀이 포인트

range 설정에 유의
각 인덱스를 순회하면서 해당 인덱스(i) 이후 인덱스를 한번 더 순회
count값을 올리다가 i보다 작아질 때 반복문을 탈출하면 된다.
"""
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
