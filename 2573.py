# 가로: m, x, i
# 세로: n, y, j

import sys

sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def melt():
    melt_ice = []
    for i in range(m):
        for j in range(n):
            sea = 0
            if graph[j][i] > 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if graph[ny][nx] <= 0:
                        sea += 1
                melt_ice.append([i, j, sea])
    for melting in melt_ice:
        graph[melting[1]][melting[0]] -= melting[2]


def dfs(x, y, visited):
    visited[y][x] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] > 0 and visited[ny][nx] == False:
            visited[ny][nx] = True
            dfs(nx, ny, visited)


def count_ice():
    visited = [[False] * m for _ in range(n)]
    ice = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] > 0 and visited[j][i] == False:
                ice += 1
                dfs(i, j, visited)
    return ice


def check_high():
    maximum = 0
    for j in range(n):
        maximum = max(maximum, max(graph[j]))
    return maximum


year = 0
isSeperate = False

while True:
    # print('ice:',count_ice())
    # print('high:',check_high())
    if count_ice() >= 2:
        break
    if check_high() <= 0:
        isSeperate = True
        break
    melt()
    year += 1

if isSeperate:
    print(0)
else:
    print(year)
