# n*m 크기의 2차원 배열이 주어졌을 때, 각 행의 최솟값들 중 최댓값 구하기

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

maximum = 0
for row in cards:
    if min(row) > maximum:
        maximum = min(row)

print(maximum)
