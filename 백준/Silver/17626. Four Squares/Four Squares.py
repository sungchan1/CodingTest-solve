from sys import stdin as s, stdout as o

# s = open("input.txt", "r")

n = int(s.readline())
result = 0
lagrange_numbers = [float("inf")] * (n+1)

for i in range(1, n+1):
    k = int(i ** 0.5)
    if k**2 == i :
        lagrange_numbers[i] = 1
        continue
    for j in range(k, 0, -1):
        # print(i, k, j, i-j**2)
        lagrange_numbers[i] = min(lagrange_numbers[i], lagrange_numbers[i-j**2]+1)
        if lagrange_numbers[i] == 2:
            break
print(lagrange_numbers[n])


