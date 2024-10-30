import heapq
from sys import stdin



child = []
n = 9
for _ in range(n):
    child.append(int(stdin.readline()))

child.sort()

amount = sum(child)
child_set = set(child)
erase = amount - 100




index = 0
value = 0

for i in range(n):
    if erase - child[i] in child_set:
        index = i
        value = erase - child[i]



for i in range(n):
    if i == index or child[i] == value:
        continue
    print(child[i])