# dir
# 701
# 6 2
# 543
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())  # r=row, c=col, m:질량, d:방향, s:속력
    graph[r - 1][c - 1].append([m, s, d])

# print(graph)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def move(x, y):
    while graph[y][x]:
        fire = graph[y][x].pop()
        m, s, d = fire[0], fire[1], fire[2]
        nx = (x + (s * dx[d])) % n
        ny = (y - (s * dy[d])) % n
        fireball[ny][nx].append([m, s, d])


def divide(x, y):
    m = 0
    cnt = 0
    s = 0
    odd = 0
    even = 0
    for fire in fireball[y][x]:
        m += fire[0]
        cnt += 1
        s += fire[1]
        if fire[2] % 2 == 0:
            even += 1
        else:
            odd += 1
    new_fire = [[m // 5, s // cnt] for _ in range(4)]

    if odd == len(fireball[y][x]) or even == len(fireball[y][x]):
        for i in range(4):
            new_fire[i].append(2 * i)
    else:
        for i in range(4):
            new_fire[i].append(2 * i + 1)
    graph[y][x] = new_fire
    if m // 5 == 0:
        graph[y][x] = []


for _ in range(k):
    fireball = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if len(graph[j][i]) != 0:
                move(i, j)

    # print(fireball)

    for i in range(n):
        for j in range(n):
            if len(fireball[j][i]) > 1:
                divide(i, j)
            else:
                graph[j][i] = fireball[j][i]
    # print(graph)

    answer = 0
    for i in range(n):
        for j in range(n):
            if len(graph[j][i]) > 1:
                for fire in graph[j][i]:
                    answer += fire[0]
            elif len(graph[j][i]) == 1:
                answer += graph[j][i][0][0]
print(answer)



