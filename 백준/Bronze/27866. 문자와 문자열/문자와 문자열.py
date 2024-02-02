from sys import stdin as s
# s =open("input.txt","r")
string = s.readline().rstrip()
print(string[int(s.readline())-1])