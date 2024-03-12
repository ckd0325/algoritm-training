# 전형적인 서로소 집합 알고리즘 사용 문제

def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
      parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
      parent[b] = a
  else:
      parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
  parent[i] = i

for _ in range(m):
  x, y, z = map(int, input().split())

  if x == 0:
    print("{}   {}".format(y, z))
    union_parent(parent, y, z)
  elif x == 1:
    if find_parent(parent, y) == find_parent(parent, z):
      print("YES")
    else:
      print("NO")