from collections import deque
from sys import stdin as s, stdout as o

# s = open("input.txt", "r")

n, test_case = map(int, s.readline().split())
numbers = list(map(int, s.readline().split()))
cumulative_sum = [0] * (len(numbers) +1)
cumulative_sum[0] = 0
for index in range(1, len(numbers)+1):
    cumulative_sum[index] = cumulative_sum[index-1] + numbers[index-1]

# print(cumulative_sum)
for test in range(test_case):
    start, end = map(int, s.readline().split())
    print(cumulative_sum[end]- cumulative_sum[start-1])
