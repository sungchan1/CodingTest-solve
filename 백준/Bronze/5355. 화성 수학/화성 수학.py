test_case = int(input())
for test in range(test_case):
    calculates = list(input().split())
    number: float = float(calculates[0])
    for calcul in calculates[1:]:
        match calcul:
            case "@":
                number = number * 3
            case "%":
                number = number + 5
            case "#":
                number = number - 7
    print("{0:.2f}".format(number))


