# https://school.programmers.co.kr/learn/courses/30/lessons/42586

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
