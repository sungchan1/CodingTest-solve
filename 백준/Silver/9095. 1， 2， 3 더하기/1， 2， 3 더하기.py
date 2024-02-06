from collections import deque
from sys import stdin as s
# s = open("input.txt", "r")
max_number = 11

dp = {}
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

test_case = int(s.readline())

for test in range(test_case):
    print(dp[int(s.readline())-1])