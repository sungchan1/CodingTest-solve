from functools import lru_cache
from sys import stdin


@lru_cache
def pow(i: int):
    return 2**i

n = int(stdin.readline())

numbers = list(map(int, stdin.readline().split()))
modular = 1_000_000_007

numbers.sort()

result = 0

for i in range(n):
    max_count = pow(i)

    result += ((numbers[i] % modular) * max_count) % modular
    min_count = pow(n-i-1)

    result -= ((numbers[i] % modular) * min_count) % modular
    
    result %= modular

print(result)









