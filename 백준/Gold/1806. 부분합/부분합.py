import time
from sys import stdin as s

# s = open("input.txt", "r")
n, target_sum = map(int, s.readline().split())
numbers = list(map(int, s.readline().split()))
min_len = float("inf")

start, end = 0,0
current_sum = numbers[0]
current_len = 0
while True:
    if current_sum < target_sum:
        end +=1
        if end == n : break
        current_sum += numbers[end]
    else:
        min_len = min(min_len, end-start+1)
        current_sum -= numbers[start]
        start +=1


min_len = 0 if min_len == float("inf") else min_len
print(min_len)