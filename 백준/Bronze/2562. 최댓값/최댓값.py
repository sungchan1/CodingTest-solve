numbers = list()
for test in range(9):
    numbers.append(int(input()))

max_value = max(numbers)
index = numbers.index(max_value)

print(max_value)
print(index+1)
