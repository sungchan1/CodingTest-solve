from sys import stdin as s

test_case = int(s.readline())

result = 1
for test in range(test_case):
    result += int(s.readline())-1
    
print(result)