# https://www.acmicpc.net/problem/2501

def max(nums:list):
    num = nums[0]
    for i in nums:
        if(num < i): num = i
    
    return num

def min(nums:list):
    num = nums[0]
    for i in nums:
        if(num > i): num = i
    
    return num

test_count = int(input())
nums = list(map(int, input().split()))

print(f"{min(nums)} {max(nums)}")