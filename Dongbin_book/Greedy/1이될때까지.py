# n이 1이 될 때까지 다음 두가지 연산을 했을 때 나올 수 있는 연산 횟수의 최솟값
# 1. n에서 1을 뺀다
# 2. k로 나눈다. 단, n이 k로 나누어 떨어질 때만 가능

n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1
    count += 1

print(count)
