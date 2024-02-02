from sys import stdin as s
# s =open("input.txt","r")
test_case = int(s.readline())
for test in range(test_case):
    string = s.readline().rstrip()
    print(string[0]+string[-1])