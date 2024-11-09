from sys import stdin



first = " " +stdin.readline().strip()
second = " " +stdin.readline().strip()

n = len(first)
m = len(second)
dp = [
    [0] * m
    for _
    in range(n)
]

for i in range(1,n):
    for j in range(1,m):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[n-1][m-1])


