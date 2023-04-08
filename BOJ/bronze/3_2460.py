# https://www.acmicpc.net/problem/2460

passengers = [list(map(int, input().split())) for _ in range(10)]

curr_num = passengers[0][1]
maximum = 0
for i in range(1,10):
    curr_num = curr_num + passengers[i][1] - passengers[i][0]
    if maximum < curr_num:
        maximum = curr_num

print(maximum)