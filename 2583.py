from collections import deque
m,n,k=map(int,input().split())
#m 세로(y,j) n:가로(x,i)
graph=[[0]*(n) for _ in range(m)]

for _ in range(k):
  x1,y1,x2,y2=list(map(int,input().split()))
  for i in range(x1,x2):
    for j in range(y1,y2):
      graph[j][i]=1
#print(graph)

def bfs(x,y):
  area=1
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  graph[y][x]=1
  q=deque([[x,y]])
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<m and graph[ny][nx]==0:
        area+=1
        graph[ny][nx]=1
        q.append([nx,ny])
  return area

area=[]
for i in range(n):
  for j in range(m):
    if graph[j][i]==0:
      area.append(bfs(i,j))
area.sort()

print(len(area))
print(' '.join(map(str,area)))