from functools import cache
from sys import stdin


@cache
def pow(i: int):
    return (2 ** i) % modular


n = int(stdin.readline())

numbers = list(map(int, stdin.readline().split()))
modular = 1_000_000_007

powers = [1] * n
for i in range(1, n):
    powers[i] = (powers[i - 1] * 2) % modular

numbers.sort()
result = 0

for i in range(n):
    # count = (pow(i) - pow(n - i - 1)) % modular
    count = (powers[i] - powers[n - i - 1]) % modular
    target = numbers[i] % modular
    result += (target * count) % modular
    result %= modular

print(result)
