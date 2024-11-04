from sys import stdin
from heapq import heappop, heappush

n = int(stdin.readline())

homeworks = [ [] for _ in range(1_000+1)]

for _ in range(n):
    d, w = map(int, stdin.readline().split())
    homeworks[d].append(w)


q = []
result = 0
for day in range(1000, 0, -1):
    for point in homeworks[day]:
        heappush(q, -point)

    if q:
        result -= heappop(q)
print(result)




