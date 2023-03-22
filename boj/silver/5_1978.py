# https://www.acmicpc.net/problem/1978

count = int(input())
nums = list(map(int, input().split()))
not_prime_numbers = list()

for i in nums:
    if i == 1:
        not_prime_numbers.append(i)
        continue

    for j in range(2, i):
        if i%j == 0:
            not_prime_numbers.append(i)
            break
    

print(count-len(not_prime_numbers))