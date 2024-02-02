from sys import stdin as s
# s = open("input.txt", "r")

n,k = map(int, s.readline().split())
coins = []
result = 0
for i in range(n):
    coins.append(int(s.readline()))

for coin in coins[::-1]:
    result += k // coin
    k = k % coin
print(result)

