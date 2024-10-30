from collections import defaultdict
from sys import stdin


n = 5


numbers = []
count = defaultdict(int)
for i in range(n):
    number = int(stdin.readline())
    numbers.append(number)

numbers.sort()

# 산술평균
print(int(round(sum(numbers)/ n,0)))


# 중앙값
print(numbers[n//2])






