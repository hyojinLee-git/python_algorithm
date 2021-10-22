# 세로,가로
import sys
from collections import deque

sys.setrecursionlimit(int(1e9))

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visited[y][x] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
            graph[ny][nx] = 2
            visited[ny][nx] = True
            dfs(nx, ny)


def melt():
    cheeses = deque([])
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 2:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                        cheeses.append([nx, ny])
    return cheeses


def check_cheese():
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                return True
    return False


hour = 0
while check_cheese():
    cheese_s = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                visited[j][i] = True
                cheese_s += 1

    dfs(0, 0)
    hour += 1
    cheeses = melt()
    while cheeses:
        x, y = cheeses.popleft()
        graph[y][x] = 2

print(hour)
print(cheese_s)
# print(graph)