from collections import deque
from sys import stdin as s
# s = open("input.txt", "r")

test_case = int(s.readline())

for test in range(test_case):
    clothes_number = int(s.readline())
    closet = {}
    for i in range(clothes_number):
        clothes_name, clothes_type = s.readline().split()
        if clothes_type in closet:
            closet[clothes_type].append(clothes_name)
        else:
            closet[clothes_type] = [clothes_name]
    result = 1
    for i in closet.values():
        result *= len(i)+1
    print(result - 1)