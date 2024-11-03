from sys import stdin
from heapq import heappush, heappop



n = int(input())

q = []

for _ in range(n):
    heappush(q, int(input()))


count = 0
while len(q) > 1:
    deck_A = heappop(q)
    deck_B = heappop(q)
    deck_C = deck_A + deck_B
    count += deck_C
    heappush(q, deck_C)

print(count)




