from sys import stdin as s
number = int(s.readline())
if number in [0,1]:
    print(1)
else:
    result = 1
    for i in range(1, number+1):
        result *= i
    print(result)


