from sys import stdin as s
import math
# s=open("input.txt","rt")

s.readline()
numbers = list(map(int, s.readline().split()))
result = len(numbers)
for number in numbers :
    if number == 1 :
        result -=1
        continue
    for divisor in range(2, int(math.sqrt(number))+1):
        if number % divisor == 0:
            result -=1
            break
print(result)



