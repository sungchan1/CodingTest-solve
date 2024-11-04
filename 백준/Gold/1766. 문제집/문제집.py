from sys import stdin
from heapq import heappop, heappush

n, m = map(int, stdin.readline().split())

graph = [set() for _ in range(n + 1)]
q = []
degree = [0] * (n + 1)

for _ in range(m):
    pre, post = map(int, stdin.readline().split())
    graph[pre].add(post)
    degree[post] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        heappush(q, i)

result = ""

while q:
    problem = heappop(q)
    result += str(problem) + " "

    for next in graph[problem]:
        degree[next] -= 1
        if degree[next] == 0:
            heappush(q, next)

print(result.strip())
