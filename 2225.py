n, k = map(int, input().split())
dp = [[0] * 200 for _ in range(200)]

for i in range(200):
    dp[i][0] = i + 1
    dp[0][i] = 1

for i in range(1, 200):
    for j in range(1, 200):
        dp[j][i] = dp[j][i - 1] + dp[j - 1][i]

print(dp[k - 1][n - 1] % 1000000000)
