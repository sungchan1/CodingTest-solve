import heapq
from sys import stdin

n = int(stdin.readline())
q: list[tuple[int, int]] = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    q.append((x,y))


q.sort(key=lambda x: (x[1], x[0] ))



for point in q:
    print(point[0], point[1])