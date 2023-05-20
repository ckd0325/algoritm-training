# https://school.programmers.co.kr/learn/courses/30/lessons/42842

"""
풀이 포인트:

1부터 노란 타일 수까지 순회한다.
만약 i번째에서 노란 타일 수가 i로 나눠 떨어진다면 높이(너비)가 i인 노랑색 직사각형을 만들 수 있다.
이를 안다면 현재 노랑 직사각형을 감싸는데 필요한 갈색 타일 수를 구할 수 있다.
구한 갈색 타일 수가 brown과 일치한다면 현재 카펫의 가로, 세로를 구하면 된다.
"""
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
