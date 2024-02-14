from collections import deque
from sys import stdin as s
# s = open("input.txt", "r")

lines = int(s.readline())
numbers = []
max_dp = [0,0,0]
min_dp = [0,0,0]
for line in range(lines) :
    a,b,c = map(int, s.readline().split())

    # max
    max_dp[0] += a
    max_dp[1] += b
    max_dp[2] += c
    # min
    min_dp[0] += a
    min_dp[1] += b
    min_dp[2] += c

    max_dp[0] = max(max_dp[0], max_dp[1])
    max_dp[2] = max(max_dp[1], max_dp[2])
    max_dp[1] = max(max_dp[0], max_dp[2])

    min_dp[0] = min(min_dp[0], min_dp[1])
    min_dp[2] = min(min_dp[1], min_dp[2])
    min_dp[1] = min(min_dp[0], min_dp[2])


print(max_dp[1])
print(min_dp[1])


