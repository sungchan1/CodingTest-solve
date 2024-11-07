from sys import stdin
from bisect import bisect_left
from collections import deque

N = int(stdin.readline())

q = []
numbers = list(map(int, stdin.readline().split()))
positions = []



for number in numbers:

    index = bisect_left(q, number)
    if index == len(q):
        q.append(number)
    else :
        q[index] = number
    positions.append(index)



LIS = [0] * len(q)
target = len(q) - 1

for i in range(N-1, -1, -1):
    if target == positions[i]:
        LIS[target] = numbers[i]
        target -= 1


print(len(q))
print(" ".join(map(str,LIS)))



