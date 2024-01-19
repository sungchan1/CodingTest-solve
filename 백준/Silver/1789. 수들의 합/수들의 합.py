target_sum = int(input())
number = 0
number_sum = 0
result = 0

while number_sum < target_sum:
    number += 1
    number_sum += number
    if number_sum == target_sum:
        result = number
        break
    elif number_sum  < target_sum:
        result = number

print(result)


