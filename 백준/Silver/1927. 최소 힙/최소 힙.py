import heapq
from sys import stdin as s, stdout as o
# s = open("input.txt", "r")
test_case = int(s.readline())
q = []
for test in range(test_case):
    input_data = int(s.readline())
    if input_data == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, input_data)










