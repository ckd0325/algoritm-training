# https://www.acmicpc.net/problem/2581

def is_prime(num:int):
    if num == 1:
        return False
    
    for j in range(2,int(i/2)+1):
        if i%j == 0: return False
    
    return True

start, end = [int(input()) for _ in range(2)]
prime_numbers = list()

for i in range(start, end+1):
    if is_prime(i): prime_numbers.append(i)

if not prime_numbers: print(-1)
else: print(f"{sum(prime_numbers)}\n{prime_numbers[0]}")