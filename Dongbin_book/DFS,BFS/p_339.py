from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호 받기
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 만약 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

answer = [i for i in range(len(distance)) if distance[i] == k]

if not answer:
    print("-1")
else:
    for a in answer:
        print(a)