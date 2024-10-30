import heapq
from sys import stdin


n = int(stdin.readline())

arr_a = list(map(int, stdin.readline().split()))
arr_b = list(map(int, stdin.readline().split()))

arr_b.sort()
arr_a.sort()


result = 0
for i in range(n):
    result += arr_a[i]*arr_b[n-1-i]

print(result)



