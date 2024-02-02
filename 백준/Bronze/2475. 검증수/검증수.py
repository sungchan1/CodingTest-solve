from sys import stdin as s
# s =open("input.txt","r")
numbers = list(map(int, s.readline().split()))
result = 0
for number in numbers :
    result = (result + number**2 % 10) % 10

print(result)
