from sys import stdin as s
# s = open("input.txt", "r")

DP = {}
def fibonacci(number: int, call_zero: int, call_one: int) -> (int, int, int) :
    if (number == 0) :
        return (0,call_zero+1, call_one)
    elif (number == 1):
        return (1,call_zero, call_one+1)
    elif number in DP.keys():
        return DP[number]
    else :
        result = [_a + _b for _a, _b in zip(fibonacci(number - 1, 0, 0), fibonacci(number - 2,0,0))]
        result[1] += call_zero
        result[2] += call_one
        DP[number] = tuple(result)
        return DP[number]

test_case = int(s.readline())

for test in range(test_case):
    number = int(s.readline())
    print(" ".join(map(str, fibonacci(number,0,0)[1:])))
