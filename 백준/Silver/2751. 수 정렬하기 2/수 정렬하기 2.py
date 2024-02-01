from sys import stdin as s
import heapq
# s=open("input.txt","rt")

test_case = int(s.readline())
q = []
for test in range(test_case):
    heapq.heappush(q, int(s.readline()))

while q:
    print(heapq.heappop(q))