# https://school.programmers.co.kr/learn/courses/30/lessons/42586

"""
풀이 포인트

progresses가 빌 때까지 반복
    각 진도에 각 작업속도를 더해준다.
    progresses가 비어있지 않고 가장 앞 인덱스의 값이 100보다 큰 경우 계속 반복:
        progresses, speeds의 가장 앞 인덱스를 삭제하고 순회마다 배포된 기능 수를 1씩 올려준다.
    반복문 탈출 시의 배포 기능 수가 해당 날의 배포된 기능 수. 이를 answer에 삽입한다.
"""
def solution(progresses, speeds):
    answer = []

    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        j = 0
        while progresses and progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            j += 1

        if j != 0:
            answer.append(j)

    return answer
