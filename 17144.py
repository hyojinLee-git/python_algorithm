import sys

input = sys.stdin.readline
row, col, t = map(int, input().split())

graph = []
for _ in range(row):
    graph.append(list(map(int, input().split())))

machine = []

for i in range(col):
    for j in range(row):
        if graph[j][i] == -1:
            machine.append([i, j])
machine.sort(key=lambda x: x[1])
up = machine[0]
down = machine[1]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def diffusion(x, y):
    cnt = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < col and 0 <= ny < row and graph[ny][nx] != -1:
            graph[ny][nx] += isDust[y][x] // 5
            cnt += 1
    graph[y][x] -= cnt * (isDust[y][x] // 5)


def rotate():
    temp1 = graph[0][0]
    temp2 = graph[row - 1][col - 1]
    graph[up[1]][up[0]] = 0
    graph[down[1]][down[0]] = 0

    # 위쪽 회전
    for i in range(4):
        if i == 0:  # 위
            for j in range(1, col):
                graph[0][j - 1] = graph[0][j]
        elif i == 1:  # 오른
            for j in range(up[1]):
                graph[j][col - 1] = graph[j + 1][col - 1]
        elif i == 2:  # 아래
            for j in range(col - 1, 0, -1):
                graph[up[1]][j] = graph[up[1]][j - 1]
        elif i == 3:  # 왼
            for j in range(up[1], 0, -1):
                graph[j][0] = graph[j - 1][0]
    graph[1][0] = temp1
    graph[up[1]][up[0]] = -1

    # 아래 회전
    for i in range(4):
        if i == 0:  # 왼
            for j in range(down[1] + 1, row - 1):
                graph[j][i] = graph[j + 1][i]
        elif i == 1:  # 아래
            for j in range(col - 1):
                graph[row - 1][j] = graph[row - 1][j + 1]
        elif i == 2:  # 오른
            for j in range(row - 1, down[1], -1):
                graph[j][col - 1] = graph[j - 1][col - 1]
        elif i == 3:  # 위
            for j in range(col - 1, 0, -1):
                graph[down[1]][j] = graph[down[1]][j - 1]
    graph[row - 1][col - 2] = temp2
    graph[down[1]][down[0]] = -1


for _ in range(t):
    isDust = [[False] * col for _ in range(row)]
    for i in range(col):
        for j in range(row):
            if graph[j][i] > 0:
                isDust[j][i] = graph[j][i]

    for i in range(col):
        for j in range(row):
            if isDust[j][i] != False:
                diffusion(i, j)
    # print('diff')
    # print(graph)
    # print('rotate')
    rotate()
    # print(graph)

sum = 0
for j in range(row):
    for i in range(col):
        sum += graph[j][i]
print(sum + 2)