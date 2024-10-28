from heapq import heappush, heappop, heapify
from sys import stdin


n, k = map(int, input().split())



# 보석과 가방을 오름차순
# 무게 순
jewelry = []
bags = []
for _ in range(n):
    weight, price = map(int, input().split())
    heappush(jewelry, (weight, -price))



for _ in range(k):
    heappush(bags, int(input()))

cost = 0
j = 0
backup = []
pq = []


# 가방, 보석 (무게)

while bags:
    bag = heappop(bags)
    while jewelry and jewelry[0][0] <= bag:
        heappush(pq, heappop(jewelry)[1])
    if pq:
        cost -= heappop(pq)


print(cost)




