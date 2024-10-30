import heapq
from sys import stdin

n = int(stdin.readline())
q = [0] * 10_001

for _ in range(n):
    q[int(stdin.readline())] += 1

for i in range(1,10_001):
    for count in range(q[i]):
        print(i)

