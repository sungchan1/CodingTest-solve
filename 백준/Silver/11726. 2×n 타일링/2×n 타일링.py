from collections import deque
from sys import stdin as s, stdout as o

# s = open("input.txt", "r")

n = int(s.readline())

if n == 1 or n == 2:
    print(n)
else:
    rectangles = [0] * n
    rectangles[0] = 1
    rectangles[1] = 2

    for index in range(2, len(rectangles)):
        rectangles[index] = (rectangles[index-1] + rectangles[index-2]) % 10007

    print(rectangles[n-1])
