n=int(input())
k=int(input())
cor=list(map(int,input().split()))

cor.sort()

dis=[]
for i in range(n-1):
  dis.append(cor[i+1]-cor[i])
dis.sort()

dis=dis[:n-k]
answer=sum(dis)
print(answer)