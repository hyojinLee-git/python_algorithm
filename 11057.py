n = int(input())

d = [[0] * 10 for i in range(n + 1)]
# print(d)

for i in range(10):
    d[0][i] = 1

for i in range(1, n + 1):
    for j in range(10):
        for col in range(j + 1):
            d[i][j] += d[i - 1][col]
print(d[n][9] % 10007)