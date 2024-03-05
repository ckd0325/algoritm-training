# p.178
# 팁: 기본적인 정렬 메소드를 사용하는게 가장 편함

n = int(input())

array = [int(input()) for _ in range(n)]

def sort(arr):
  return sorted(arr)

for i in array:
  print(i, end=' ')