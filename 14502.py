from collections import deque
from itertools import combinations
import copy
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
# n: 세로,y,j
# m: 가로,x,i

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# print(graph)

empty = []
start = []
for i in range(m):
    for j in range(n):
        if graph[j][i] == 0:
            empty.append([i, j])
        if graph[j][i] == 2:
            start.append([i, j])
# print(empty)

wall = deque()
for i in combinations(empty, 3):
    wall.append(i)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs_virus():
    q = deque(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph_temp[ny][nx] == 0:
                q.append([nx, ny])
                graph_temp[ny][nx] = 2


def bfs_area():
    area = 0
    for i in range(m):
        for j in range(n):
            if graph_temp[j][i] == 0:
                graph_temp[j][i] = 3
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    area += 1
                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]
                        if 0 <= nx < m and 0 <= ny < n and graph_temp[ny][nx] == 0:
                            q.append([nx, ny])
                            graph_temp[ny][nx] = 3
    return area


max_area = 0
# print(wall[0])
for a in range(len(wall)):
    graph_temp = copy.deepcopy(graph)
    w = wall.popleft()

    # 벽 세우기
    for b in range(3):
        i, j = w[b]
        graph_temp[j][i] = 1
    # 바이러스 퍼트리기
    bfs_virus()
    # 안퍼진 영역 구하기
    area = bfs_area()

    # 최대값 갱신
    if area > max_area:
        graph_max = graph_temp
        max_area = area
print(max_area)