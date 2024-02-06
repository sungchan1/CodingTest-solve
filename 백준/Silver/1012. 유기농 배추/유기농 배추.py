from collections import deque
from sys import stdin as s, stdout as o
# s = open("input.txt", "r")
test_case = int(s.readline())
for test in range(test_case):
    width, length, vegetables_number = map(int, s.readline().split())
    vegetables_map = {}
    q = deque()

    for vegetable in range(vegetables_number):
        x,y = map(int, s.readline().split())
        vegetables_map[(x,y)] = [1, False]
        q.append((x,y))

    result = 0
    while q:
        x,y = q.popleft()
        count, visited = vegetables_map[(x,y)]
        if visited :
            continue
        result += count
        vegetables_map[(x, y)][1] = True
        if y > 0 and (x,y-1) in vegetables_map: # 상단
            if not vegetables_map[(x,y-1)][1]:
                q.remove((x,y-1))
                q.appendleft((x,y-1))
                vegetables_map[(x,y-1)][0] = 0
        if x > 0 and (x-1,y) in vegetables_map: # 좌측
            if not vegetables_map[(x-1,y)][1]:
                q.remove((x-1,y))
                q.appendleft((x-1,y))
                vegetables_map[(x-1,y)][0] = 0
        if y < length-1 and (x,y+1) in vegetables_map:  #하단
            if not vegetables_map[(x,y+1)][1]:
                q.remove((x,y+1))
                q.appendleft((x,y+1))
                vegetables_map[(x,y+1)][0] = 0
        if x < width-1 and (x+1,y) in vegetables_map : # 우측
            if not vegetables_map[(x+1,y)][1]:
                q.remove((x+1,y))
                q.appendleft((x+1,y))
                vegetables_map[(x+1,y)][0] = 0
    print(result)









