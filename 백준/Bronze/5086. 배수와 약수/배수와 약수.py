
while True:
    number_1, number_2 = map(int, input().split())

    result: str = ""
    if number_1 * number_2 == 0:
        break
    elif number_1 % number_2 == 0:
        result = "multiple"
    elif number_2 % number_1 == 0:
        result = "factor"
    else:
        result = "neither"

    print(result)
