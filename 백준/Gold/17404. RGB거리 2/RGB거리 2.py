from sys import stdin as s
# s=open("input.txt","rt")

house_number = n=int(s.readline())
# print(house_number)

MAX_COST = 1000
answer = (MAX_COST+1) * house_number
costs = list()

for house in range(house_number):
    costs.append(list(map(int,s.readline().split())))

for start in range(3):
    DP = [[MAX_COST+1, MAX_COST+1, MAX_COST+1] *3 for i in range(house_number)]
    DP[0][start] = costs[0][start]
    for house in range(1, house_number):
        DP[house][0] =  min(DP[house-1][1], DP[house-1][2])+ costs[house][0]
        DP[house][1] =  min(DP[house-1][0], DP[house-1][2])+ costs[house][1]
        DP[house][2] =  min(DP[house-1][0], DP[house-1][1])+ costs[house][2]
    for last_color in range(3):
        if start != last_color:
            answer = min (answer, DP[-1][last_color])
print(answer)

