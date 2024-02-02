from sys import stdin as s
number = int(s.readline())
numbers = list(s.readline().split())
target = s.readline().rstrip()
print(numbers.count(target))
