n=int(input())

d=[[0]*2 for i in range(n+1)]

d[1][1]=1

for i in range(2,n+1):
  d[i][0]=sum(d[i-1])
  d[i][1]=d[i-1][0]

print(sum(d[-1]))
