# https://www.acmicpc.net/problem/1789

s = int(input())
sum_val = 0

for i in range(1, s+1):
    sum_val += i
    if sum_val == s:
        print(i)
        break
    if sum_val > s:
        print(i-1)
        break
