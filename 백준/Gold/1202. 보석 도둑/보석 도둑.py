from heapq import heappush, heappop, heapify
from sys import stdin


n, k = map(int, stdin.readline().split())



jewelry = []
bags = []
for _ in range(n):
    weight, price = map(int, stdin.readline().split())
    heappush(jewelry, (weight, -price))



for _ in range(k):
    heappush(bags, int(stdin.readline()))

cost = 0
j = 0
backup = []
pq = []
while bags:
    bag = heappop(bags)
    while jewelry and jewelry[0][0] <= bag:
        heappush(pq, heappop(jewelry)[1])
    if pq:
        cost -= heappop(pq)
    # print(cost)


print(cost)




