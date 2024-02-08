from sys import stdin as s
# s = open("input.txt", "r")
house_number = int(s.readline())
costs = []
dp = [ [float("inf")] * 3 for house in range(house_number)]
for house in range(house_number):
    costs.append(list(map(int, s.readline().split())))

dp[0][0]= costs[0][0]
dp[0][1]= costs[0][1]
dp[0][2]= costs[0][2]

for i in range(1, house_number):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[-1]))

