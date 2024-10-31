import heapq
from sys import stdin


n = int(stdin.readline())



numbers = list(map(int, stdin.readline().split()))
numbers_sort = sorted(list(set(numbers)))
hash_dict = dict()

for i in range(len(numbers_sort)):
    hash_dict[numbers_sort[i]] = i




for number in numbers:
    print(hash_dict[number], end=" ")
