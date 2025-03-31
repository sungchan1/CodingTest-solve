from sys import stdin

input = stdin.readline


n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

t_shirt_bundle = 0
pen_bundle = 0
pen_single = 0

for size in sizes:
    if size % t == 0:
        t_shirt_bundle += size // t
    else:
        t_shirt_bundle += size // t + 1


pen_bundle = n // p
pen_single = n % p

print(t_shirt_bundle)
print(pen_bundle, pen_single)