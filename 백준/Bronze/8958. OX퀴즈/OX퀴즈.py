test_number = int(input())


for i in range(test_number):
    scores = input()
    result = 0
    point = 1

    for score in scores:
        if score == "O" :
            result += point
            point += 1
        elif score == "X":
            point = 1
    print(result)