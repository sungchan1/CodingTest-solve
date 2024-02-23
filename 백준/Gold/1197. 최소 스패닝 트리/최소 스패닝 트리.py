import heapq
import sys
from sys import stdin as s

# s = open("input.txt", "r")

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


vertex_number, edge_number = map(int, s.readline().split())

edges = []

for edge in range(edge_number):
    start, end, cost = map(int, s.readline().split())
    heapq.heappush(edges, (cost, start-1, end-1))



path_number = 0
parent = [i for i in range(vertex_number)]
result = 0
while edges and  path_number < (vertex_number-1):
    cost, start, end = heapq.heappop(edges)
    if find_parent(parent, start) != find_parent(parent, end ):
        union(parent, start, end)
        result += cost
        path_number += 1
print(result)

