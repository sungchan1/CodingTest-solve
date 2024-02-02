from sys import stdin as s
# s =open("input.txt","r")
a,b= map(int, s.readline().split())
print((a+b)*(a-b))