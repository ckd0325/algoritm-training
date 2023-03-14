# https://www.acmicpc.net/problem/10870
# 대표적 재귀 문제

def fibo(n:int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

n = int(input())
    
print(fibo(n))