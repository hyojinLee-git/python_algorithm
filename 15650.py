n,m=map(int,input().split())

lst=[0]*(m+1)

def solution(x):
  if x==m+1:
    for i in range(1,m+1):
      print(lst[i],end=' ')
    print()
  else:
    for i in range(1,n+1):  #모든 자식노드
      if max(lst)<i:
        lst[x]=i
        solution(x+1)
        lst[x]=0  #부모 노드로 돌아감


solution(1)