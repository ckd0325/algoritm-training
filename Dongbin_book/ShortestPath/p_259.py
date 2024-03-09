# 플로이드 워셜 알고리즘을 사용하는 전형적인 유형
# 본인은 다익스트라로 풀이하였다.

import heapq

INF = int(1e9)



def dijkstra(start, graph, n):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return distance

def my_answer():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    x, k = map(int, input().split())

    path1 = dijkstra(1, graph, n)
    path2 = dijkstra(k, graph, n)

    if path1[k] == INF or path2[x] == INF:
        print("-1")
    else:
        print(dijkstra(1)[k] + dijkstra(k)[x])

def book_answer():
    n, m = map(int, input().split())
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split)
        graph[a][b] = 1
        graph[b][a] = 1

    x, k = map(int, input().split())

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    distance = graph[1][k] + graph[k][x]

    if distance >= INF:
        print("-1")
    else:
        print(distance)