from sys import stdin
from heapq import heappop, heappush



n = int(stdin.readline())



parent =  list(map(int, stdin.readline().split()))
tree =  list(map(int, stdin.readline().split()))


tree.sort(key=lambda x: -x)


result = 0

for i in range(len(tree)):
    result += tree[i]
    print(result)
