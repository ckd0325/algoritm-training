# 전형적인 크루스칼 알고리즘 사용문제
# 최소신장트리를 만들고 가장 비용이 높은 곳을 없애면 최소한의 비용이 되게 분리됨

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

edges = []
last = 0
result = 0

for i in range(n+1):
  parent[i] = i

for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    last = cost

print(result - last)