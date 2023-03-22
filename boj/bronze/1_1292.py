# https://www.acmicpc.net/problem/1292

import sys

start, end = map(int, input().split())
arr = list()

for i in range(1, sys.maxsize):
    temp_arr = [i] * i
    arr.extend(temp_arr)

    if len(arr) > 1000: break

print(sum(arr[start-1:end]))