from sys import stdin as s, stdout as o

# s = open("input.txt", "r")

n = int(s.readline())
result = 0
lagrange_numbers = [4] * (n+1)
squares = [i**2 for i in range(int(n**0.5)+1)]
for i in range(1, n+1):
    k = int(i ** 0.5)
    if k**2 == i :
        lagrange_numbers[i] = 1
        continue
    for j in range(k, 0, -1):
        lagrange_numbers[i] = min(lagrange_numbers[i], lagrange_numbers[i-squares[j]]+1)
        if lagrange_numbers[i] == 2:
            break
print(lagrange_numbers[n])