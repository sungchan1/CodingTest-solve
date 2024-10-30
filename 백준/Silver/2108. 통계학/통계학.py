from collections import defaultdict
import heapq
import math
from sys import stdin


n = int(stdin.readline())


numbers = []
count = defaultdict(int)
for i in range(n):
    number = int(stdin.readline())
    numbers.append(number)
    count[number] += 1

numbers.sort()

# 산술평균
print(int(round(sum(numbers)/ n,0)))


# 중앙값
print(numbers[n//2])

# 최빈도

max_frequency = -1
q = []
for number, frequency in count.items():
    if frequency > max_frequency:
        max_frequency = frequency
        q = [number]

    elif frequency == max_frequency:
        q.append(number)

q.sort()

if len(q) == 1:
    print(q[0])
else:
    print(q[1])



# 범위
print(numbers[n-1]-numbers[0])












