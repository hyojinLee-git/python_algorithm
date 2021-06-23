from collections import deque
import copy
import sys
n=int(sys.stdin.readline().rstrip())

graph=[]
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

#print(graph)


def bfs(high):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  area=0
  for i in range(n):
    for j in range(n):
      if graph_temp[i][j]>high:
        area+=1
        q=deque([(i,j)])
        while q:
          x,y=q.popleft()
          for a in range(4):
            nx=x+dx[a]
            ny=y+dy[a]
            if 0<=nx<n and 0<=ny<n:
              if graph_temp[nx][ny]>high:
                graph_temp[nx][ny]=0
                q.append([nx,ny])
  return area

max_high=0
for i in range(n):
  for j in range(n):
    if graph[i][j]>max_high:
      max_high=graph[i][j]

high=[(i+1) for i in range(max_high)]
max_area=0

for i in range(max_high+1):
  graph_temp=copy.deepcopy(graph)
  #print('high:',i,'area:',bfs(i))
  area=bfs(i)
  if area>max_area:
    max_area=area
print(max_area)
