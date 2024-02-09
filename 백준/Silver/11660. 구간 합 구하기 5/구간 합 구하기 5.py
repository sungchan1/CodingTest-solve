from collections import deque
from sys import stdin as s, stdout as o
# s = open("input.txt", "r")
n, m = map(int, s.readline().split())

numbers = []
dp = [[0] * (n+1) for _ in range(n+1)]

for row in range(n):
    numbers.append(list(map(int, s.readline().split())))

for row in range(1, n+1):
    for col in range(1, n+1):
        dp[row][col] = dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1] + numbers[row-1][col-1]

for test in range(m):
    x1, y1, x2, y2 = map(int, s.readline().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)

