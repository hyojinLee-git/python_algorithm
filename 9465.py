t=int(input())
for _ in range(t):

  n=int(input())
  sticker=[]


  for _ in range(2):
    sticker.append(list(map(int,input().split())))

  dp=[[0]*n for _ in range(2)]

  dp[0][0]=sticker[0][0]
  dp[1][0]=sticker[1][0]
  dp[0][1]=dp[1][0]+sticker[0][1]
  dp[1][1]=dp[0][0]+sticker[1][1]
  for j in range(2,n):
    for i in range(2):
      if i==0:
        dp[i][j]=max(dp[i+1][j-1]+sticker[i][j],sticker[i][j]+dp[i+1][j-2])
      else:
        dp[i][j]=max(dp[i-1][j-1]+sticker[i][j],sticker[i][j]+dp[i-1][j-2])
  print(max(dp[0][-1],dp[1][-1]))