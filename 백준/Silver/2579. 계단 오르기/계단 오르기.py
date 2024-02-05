from collections import deque
from sys import stdin as s


# s = open("input.txt", "r")

n = int(s.readline())
stair=[0]
for i in range(n):
    stair.append(int(s.readline()))

if len(stair) < 3:
    print(sum(stair))

else:
    dp = [0 for i in range(n+1)]
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]


    for i in range(3, len(dp)):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])










