import sys
from collections import defaultdict
input = sys.stdin.readline
n, cash = map(int, input().split())


x_gems = defaultdict(list)
y_gems = defaultdict(list)

for _ in range(n):
    x, y, v = map(int, input().split())
    x_gems[x].append((y, v))
    y_gems[y].append((x, v))

cost = 0
result = 0
value = 0
x = 100_000
y = 0

while x >= 0 and y <= 100_000:
    if cost <= cash:
        result = max(result, value)

        for _x, v in y_gems[y]:
            if _x <= x:
                cost += 1
                value += v
        y += 1
    else:
        for _y, v in x_gems[x]:
            if _y <= y:
                cost -= 1
                value -= v

        x -= 1

    if cost <= cash:
        result = max(result, value)


print(result)

