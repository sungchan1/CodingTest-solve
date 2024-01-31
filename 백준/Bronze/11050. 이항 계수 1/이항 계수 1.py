def factorial(n:int) -> int:
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum
    
n,k = map(int, input().split())

print(int(factorial(n)/(factorial(k)*(factorial(n-k)))))
