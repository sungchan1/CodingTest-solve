import heapq
from sys import stdin

n = int(stdin.readline())

numbers = list(map(int, stdin.readline().split()))
numbers_sort = sorted(set(numbers))
hash_dict = dict()

for index, key in enumerate(numbers_sort):
    hash_dict[key] = str(index)


for number in numbers:
    print(hash_dict[number], end=" ")
