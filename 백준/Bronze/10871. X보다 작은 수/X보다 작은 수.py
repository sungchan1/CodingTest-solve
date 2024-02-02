from sys import stdin as s
n,x = map(int, s.readline().split())
numbers = list(map(int, s.readline().split()))
print(' '.join([str(number) for number in numbers if number < x]))