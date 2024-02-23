from sys import stdin as s

import heapq


def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]



def uninon(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



# s = open("input.txt", "r")

n, m = map(int, s.readline().split())

paths = []
path_number = 0
result = 0
parent = [i for i in range(n)]

for path in range(m):
    start, end, cost = map(int, s.readline().split())
    heapq.heappush(paths, (cost,start-1,end-1))

while paths and  path_number < (n-2):
    cost, start, end = heapq.heappop(paths)
    if find_parent(parent, start) != find_parent(parent, end):
        uninon(parent, start,end)
        result += cost
        path_number += 1
print(result)









