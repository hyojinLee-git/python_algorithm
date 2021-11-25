n,k=map(int,input().split())

stone=list(map(int,input().split()))

dp=[False]*n
dp[0]=True
for i in range(1,n):
  for j in range(i):
    if dp[j] and (i-j)*(1+abs(stone[j]-stone[i]))<=k:
      dp[i]=True
      break
if dp[-1]:
  print('YES')
else:
  print('NO')