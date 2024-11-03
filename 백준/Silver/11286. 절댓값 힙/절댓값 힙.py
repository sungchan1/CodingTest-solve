from sys import stdin
from heapq import heappush, heappop

q = []


n = int(stdin.readline())

for _ in range(n):
    number = int(stdin.readline())
    if number == 0:
        if q:
            __, num = heappop(q)
            print(num)
        else:
            print(0)
    else :

        heappush(q, (abs(number), number))