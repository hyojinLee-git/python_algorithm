from collections import deque
row,col=map(int,input().split())
graph=[]
for _ in range(row):
  graph.append(list(input()))

doyeon=[]
visited=[[False]*col for _ in range(row)]

for i in range(col):
  for j in range(row):
    if graph[j][i]=='I':
      doyeon+=[i,j]
    elif graph[j][i]=='X':
      visited[j][i]=True

dx,dy=[1,-1,0,0],[0,0,1,-1]

def bfs(x,y):
  q=deque([[x,y]])
  visited[y][x]=True
  answer=0
  while q:
    x,y=q.popleft()
    for d in range(4):
      nx,ny=x+dx[d],y+dy[d]
      if 0<=nx<col and 0<=ny<row and not visited[ny][nx]:
        visited[ny][nx]=True
        q.append([nx,ny])
        if graph[ny][nx]=='P':
          answer+=1
  return answer

answer=bfs(doyeon[0],doyeon[1])
if answer==0:
  print('TT')
else:
  print(answer)