t=int(input())

for _ in range(t):
  dp=[]
  n,m=map(int,input().split())
  for _ in range(n):
    dp.append([0]*m)

  #n-1, m-1
  for i in range(m):
    dp[0][i]=i+1

  for i in range(1,n):
    for j in range(i-1,m):
      dp[i][j]=sum(dp[i-1][:j])
  #print(dp)
  print(dp[-1][-1])

