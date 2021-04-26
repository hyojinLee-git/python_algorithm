import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(n + 1):
    graph[i].sort()


# print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)


visited = [False] * (n + 1)
result = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        result += 1
print(result)
