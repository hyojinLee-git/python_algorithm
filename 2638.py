import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
row, col = map(int, input().split())

graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))
# print(graph)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    graph[y][x] = 2
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < col and 0 <= ny < row and visited[ny][nx] == False:
            graph[ny][nx] = 2
            visited[ny][nx] = True
            dfs(nx, ny)


def melt():
    cheese = []
    for i in range(col):
        for j in range(row):
            if graph[j][i] == 1:
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < col and 0 <= nj < row and graph[nj][ni] == 2:
                        cnt += 1
                if cnt >= 2:
                    cheese.append([i, j])
    return cheese


hour = 0

while True:
    visited = [[False] * col for _ in range(row)]
    for i in range(col):
        for j in range(row):
            if graph[j][i] == 1:
                visited[j][i] = True
    dfs(0, 0)
    cheeses = melt()
    if len(cheeses) == 0:
        break
    for cheese in cheeses:
        graph[cheese[1]][cheese[0]] = 2
    hour += 1

print(hour)

