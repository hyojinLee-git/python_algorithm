import sys

def dfs(graph,v,visited):
  visited[v]=True
  for i in graph[v]:
    if not visited[i]:
      visited[i]=True
      dfs(graph,i,visited)

t=int(sys.stdin.readline())
while t>0:
  t-=1
  n=int(sys.stdin.readline())
  graph=[[] for _ in range(n+1)]
  visited=[False]*(n+1)
  lst=list(map(int,sys.stdin.readline().split()))
  #print(lst)
  for i in range(n):
    graph[i+1].append(lst[i])
    graph[lst[i]].append(i+1)
  answer=0
  for i in range(1,n+1):
    if not visited[i]:
      answer+=1
      dfs(graph,i,visited)
      #print(visited)
  print(answer)