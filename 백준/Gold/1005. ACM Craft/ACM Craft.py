import sys
from sys import stdin as s

sys.setrecursionlimit(10000)
# s = open("input.txt", "r")
def build(build_times, rules, building_number, dp):
    if dp[building_number] != -1:
        return dp[building_number]

    build_time = 0
    if rules[building_number]:
        for rule_condition in rules[building_number]:
            build_time = max(build_time, build(build_times, rules, rule_condition, dp))

    build_time += build_times[building_number]
    dp[building_number] = build_time

    return build_time



test_case = int(s.readline())

for test in range(test_case):
    building, rule_number = map(int, s.readline().split())
    buildings = list(map(int, s.readline().split()))
    rules = [[] for i in range(building)]
    dp = [-1 for i in range(building)]
    for rule in range(rule_number):
        condition, building_number = map(int, s.readline().split())
        rules[building_number-1].append(condition-1)



    target = int(s.readline())
    print(build(buildings, rules, target-1, dp))
