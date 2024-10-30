import heapq
from sys import stdin


n = int(stdin.readline())
cards = set(map(int, stdin.readline().split()))


m = int(stdin.readline())


targets = list(map(int, stdin.readline().split()))
for target in targets:
    if target in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")



