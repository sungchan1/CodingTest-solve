from collections import deque
from sys import stdin as s
# s = open("input.txt", "r")

test_case = int(s.readline())
triangle_side =  [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for side_index in range(10, len(triangle_side)):
    triangle_side[side_index] = triangle_side[side_index-1] + triangle_side[side_index-5]

for test in range(test_case):
    print(triangle_side[int(s.readline())-1])

