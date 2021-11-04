from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

size = 2

for i in range(n):
    for j in range(n):
        if graph[j][i] == 9:
            shark = [i, j]


def get_fish():
    fish = []
    for i in range(n):
        for j in range(n):
            if graph[j][i] != 0 and graph[j][i] < size:
                dist = get_distance(i, j)
                if dist != None:
                    fish.append([i, j, dist + 1])
    fish.sort(key=lambda x: [x[2], x[1], x[0]])
    if len(fish) != 0:
        return fish[0]
    else:
        return


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def get_distance(gx, gy):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[j][i] > size:
                visited[j][i] = -1

    q = deque([shark])
    visited[shark[1]][shark[0]] = -1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                q.append([nx, ny])
                if nx == gx and ny == gy:
                    return visited[ny][nx]
    return


sec = 0
cnt = 0
while True:
    fish = get_fish()
    # print('fish:',fish)
    if not fish:
        break
    graph[shark[1]][shark[0]] = 0
    graph[fish[1]][fish[0]] = 9
    shark = [fish[0], fish[1]]
    sec += fish[2]
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
    # print(graph)
print(sec)
