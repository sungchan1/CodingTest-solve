import sys
import heapq

quiz = input().split()


a = int(quiz[0])
b = int(quiz[2])
c = int(quiz[4])

answer = "YES" if a+b == c else "NO"
print(answer)