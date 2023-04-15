# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_row = i
            y_col = yellow // i
        else:
            continue

        b_num = (y_col + 2) * 2 + y_row * 2
        if b_num == brown:
            answer.append(y_col + 2)
            answer.append(y_row + 2)
            break

    return answer
