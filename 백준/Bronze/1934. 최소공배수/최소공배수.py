def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

test_number = int(input())
for _ in range(test_number):
    number_1, number_2 = map(int, input().split())
    print(lcm(number_1, number_2))