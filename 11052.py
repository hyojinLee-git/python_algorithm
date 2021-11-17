n = int(input())
card = list(map(int, input().split()))
dp = [0] * (n + 1)

m = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        m = max(card[i - 1], card[j - 1] * (i // j), dp[j] + dp[i - j], m)

    dp[i] = m
    # print(dp)
print(dp[-1])