from sys import stdin



first = " " +stdin.readline().strip()
second = " " +stdin.readline().strip()

n = len(first)
m = len(second)
dp = [
    [""] * m
    for _
    in range(n)
]


for i in range(1,n):
    for j in range(1,m):
        if first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + first[i]

        else:
            if len(dp[i-1][j]) <= len(dp[i][j-1]):
                dp[i][j] = dp[i][j-1]

            else:
                dp[i][j] = dp[i-1][j]





print(len(dp[n-1][m-1]))
if len(dp[n-1][m-1]) != 0:
    print(dp[n-1][m-1])



