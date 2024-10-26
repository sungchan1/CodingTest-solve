
# n = int(input())
#
# points = set()
# result = float("inf")
#
# for _ in range(n):
#     x, y = map(int, input().split())
#     if (x, y) in points:
#         continue
#     for px, py in points:
#         distance = (x - px) ** 2 + (y - py) ** 2
#         result = min(result, distance)
#     points.add((x, y))
#
#
# result = 0 if result == float("inf") else result
#
# print(result)

n = int(input())

prime_check = [True] * ( n +1)

prime_check[0] = prime_check[1] = False
for i in range(2, int((n+ 1) ** 0.5)+1 ):
    if prime_check[i]:
        for j in range(i * i, n+1, i):
            prime_check[j] = False


primes = [i for i in range(2, n + 1) if prime_check[i]]

start = end = 0
count = 0
prime_sum = 0


while start < len(primes):
    if prime_sum == n:
        count += 1
        prime_sum -= primes[start]
        start += 1

    elif prime_sum > n:
        prime_sum -= primes[start]
        start += 1

    else:
        if end >= len(primes):
            break
        prime_sum += primes[end]
        end += 1

print(count)
