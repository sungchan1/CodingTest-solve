from sys import stdin as s
test_case =  int(s.readline())

for test in range(test_case):
    a, b = map(int, s.readline().split())
    print(a+b)