n=int(input())
lst=[]
for _ in range(n):
  lst.append(int(input()))

dp=[0]*n
dp[0]=lst[0]
if n>=2:
  dp[1]=lst[1]+lst[0]
if n>=3:
  dp[2]=max(lst[2]+lst[0],lst[2]+lst[1],dp[1])


for i in range(3,n):
  dp[i]=max(dp[i-1],lst[i]+dp[i-2],lst[i-1]+dp[i-3]+lst[i])
#print(lst)
#print(dp)
print(dp[-1])