from collections import deque
import sys
n,m=map(int,sys.stdin.readline().rstrip().split())

graph=[]
for _ in range(m):
  graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

q=deque()
for i in range(m):
  for j in range(n):
    if graph[i][j]==1:
      q.append([i,j])

def bfs():
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  while q:
    x,y=q.popleft()
    if graph[x][y]==-1:
      pass
    else:
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n:
          if graph[nx][ny]==0:
            graph[nx][ny]=graph[x][y]+1
            q.append([nx,ny])

bfs()
answer=0
for i in range(len(graph)):
  for j in range(n):
    if graph[i][j]>answer:
      answer=graph[i][j]

fin=True
for i in range(m):
  if 0 in graph[i]:
    fin=False
    print(-1)
    break

if fin:
  print(answer-1)
