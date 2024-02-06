from collections import deque
from sys import stdin as s, stdout as o

# s = open("input.txt", "r")

a, b = map(int, s.readline().split())
q = deque([])
q.append((a,1))
result = -1
while q:
    # print(q)
    number, count  = q.popleft()
    if number == b :
        result = count
        break

    if number *2 <= b:
        q.append([number*2, count+1])
    if int(str(number) + "1") <= b:
        q.append([int(str(number) + "1"), count+1])

print(result)
