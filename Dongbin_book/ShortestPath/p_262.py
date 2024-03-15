# 팁: 다익스트라 알고리즘을 적용하면 쉽게 풀이 가능

import heapq

INF = int(1e9)

# 책 정답과 거의 유사
def my_answer():
    n, m, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))

    def dijkstra(start):
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

    dijkstra(c)

    count = 0
    max_distance = 0

    for d in distance:
        if INF > d > 0:
            count += 1
        if max_distance < d < INF:
            max_distance = d

    print("{} {}".format(count, max_distance))

my_answer()