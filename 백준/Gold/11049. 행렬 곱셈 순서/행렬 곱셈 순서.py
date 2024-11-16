from sys import stdin

n = int(stdin.readline())

matrix = [tuple(map(int, input().split())) for i in range(n)]

dp = [[0] * n for _ in range(n)]

for diagonal in range(n-1):
    for i in range(n - diagonal-1):
        j = i + diagonal + 1
        dp[i][j] = float("inf")
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + \
                               matrix[i][0] * matrix[k][1] * matrix[j][1])




print(dp[0][-1])
