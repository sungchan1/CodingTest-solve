number_a = int(input())
operator = input()
number_b = int(input())
result = 0
match operator:
    case "+":
        result = number_a + number_b
    case "*":
        result = number_a * number_b
print(result)