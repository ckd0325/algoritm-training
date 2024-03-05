from collections import deque

n, m = map(int, input().split())
graph = list()

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >=n or graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append(nx, ny)

    return graph[n-1][m-1]

print(bfs(0,0))