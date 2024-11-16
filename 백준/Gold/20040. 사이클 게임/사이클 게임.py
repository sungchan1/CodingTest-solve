from sys import stdin

n, m = map(int, stdin.readline().split())

points = [i for i in range(n)]


def union(p1, p2):
    parent1 = find(p1)
    parent2 = find(p2)

    if parent1 > parent2:
        parent1, parent2 = parent2, parent1

    points[parent2] = parent1

def find(point):
    p = point
    while p != points[p]:
        p = points[p]
    return p


result = 0

for count in range(1, m + 1):
    p1, p2 = map(int, stdin.readline().split())


    if find(p1) == find(p2):
        result = count
        break

    union(p1, p2)





print(result)
