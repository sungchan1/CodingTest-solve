from sys import stdin
from bisect import bisect_left


N = int(stdin.readline())

q = []
numbers = list(map(int, stdin.readline().split()))

for number in numbers:

    index = bisect_left(q, number)
    if index == len(q):
        q.append(number)
    else :
        q[index] = number

print(len(q))



