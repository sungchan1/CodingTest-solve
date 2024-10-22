n = int(input())
if n == 0:
    print(n)
else:
    f1 = 0
    f2 = 1
    f3 = 1
    for i in range(n-1):
        f3 = f1+f2
        f1 = f2
        f2 = f3

    print(f3)
