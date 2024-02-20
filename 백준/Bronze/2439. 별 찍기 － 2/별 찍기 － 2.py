from sys import stdin as s
from collections import deque
# s = open("input.txt", "r")

line = int(s.readline())


for star in range(1, line+1):
    print(" "*(line-star)+"*"*star)