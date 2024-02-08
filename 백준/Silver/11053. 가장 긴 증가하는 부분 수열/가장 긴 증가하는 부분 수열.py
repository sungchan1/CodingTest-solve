from sys import stdin as s
# s = open("input.txt", "r")
s.readline()
numbers = list(map(int, s.readline().split()))
length = [1] * len(numbers)
result = 1
for i, number in enumerate(numbers):
    for k in range(i):
        if numbers[k] < number:
            length[i] = max(length[i], length[k] + 1)
            result = max(result, length[i])
print(result)
