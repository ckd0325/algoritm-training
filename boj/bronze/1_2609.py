# https://www.acmicpc.net/problem/2609
# 유클리드 호제법 참고

def get_gcd(n1, n2):

    if n1 % n2 == 0:
        return n2
    else:
        return get_gcd(n2, n1%n2)
    

nums = list(map(int, input().split()))
big_num = 0
small_num = 0

if nums[0] > nums[1]:
    big_num = nums[0]
    small_num = nums[1]
else:
    big_num = nums[1]
    small_num = nums[0]

gcd = get_gcd(big_num, small_num)
print(f"{gcd}\n{int(big_num*small_num/gcd)}")