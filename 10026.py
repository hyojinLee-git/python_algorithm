import sys
import copy

sys.setrecursionlimit(1000000)
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

graph2 = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if graph2[j][i] == 'G':
            graph2[j][i] = 'R'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, rgb, graph):
    graph[y][x] = 'W'
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == rgb:
            graph[y][x] = 'W'
            dfs(nx, ny, rgb, graph)


area = 0
area2 = 0

for i in range(n):
    for j in range(n):
        if graph[j][i] == 'R':
            dfs(i, j, 'R', graph)
            area += 1
        elif graph[j][i] == 'B':
            dfs(i, j, 'B', graph)
            area += 1
        elif graph[j][i] == 'G':
            dfs(i, j, 'G', graph)
            area += 1

        if graph2[j][i] == 'R':
            dfs(i, j, 'R', graph2)
            area2 += 1
        elif graph2[j][i] == 'B':
            dfs(i, j, 'B', graph2)
            area2 += 1

print(area, area2)