import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n = int(sys.stdin.readline())

graph = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(lst)
# print(graph)
result = 0
cnt = 0
answer = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            answer.append(cnt)
        # print(cnt)
        cnt = 0

print(result)
for i in sorted(answer):
    print(i)