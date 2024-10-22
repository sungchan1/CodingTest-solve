
fibonacci = [0,1]
divisor = 1_000_000
while True:
    next = sum(fibonacci[-2:]) % divisor
    if next == 0 and fibonacci[-1] == 1:
        break

    fibonacci.append(next)


n = int(input())

index = n % len(fibonacci)
print(fibonacci[index])