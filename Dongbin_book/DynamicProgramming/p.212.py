# 메모이제이션 기법을 이용한 피보나치 수열 구하기

d = [0] * 100

def fibo(x):

    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))