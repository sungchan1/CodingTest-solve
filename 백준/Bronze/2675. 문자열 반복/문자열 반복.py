test_number = int(input())
for i in range(test_number):
    iter_number, target_str = input().split()
    iter_number = int(iter_number)

    result = ""
    for j in range(len(target_str)):
        result += target_str[j] * iter_number
    print(result)