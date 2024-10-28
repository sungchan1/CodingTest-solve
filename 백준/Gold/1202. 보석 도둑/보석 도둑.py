from heapq import heappush, heappop, heapify
from sys import stdin


n, k = map(int, stdin.readline().split())



# 보석과 가방을 오름차순
# 무게 순
jewelry = []
bags = []
for _ in range(n):
    weight, price = map(int, stdin.readline().split())
    jewelry.append((weight, -price))



for _ in range(k):
    bags.append(int(stdin.readline()))

cost = 0
j = 0
backup = []
pq = []

jewelry.sort()
bags.sort()

# 가방, 보석 (무게)
j = 0
for bag in bags:
    while j < n and jewelry[j][0] <= bag:
        heappush(pq, jewelry[j][1])
        j +=1
    if pq:
        cost -= heappop(pq)

print(cost)




