from functools import lru_cache

def calcul(number):
    DP ={1:0}
    
    for n in range(2, number+1):
        temp = DP[n-1] +1
        if n % 3 == 0:
            temp = min(temp, DP[n//3] +1)
        if n % 2 == 0:
            temp = min(temp, DP[n//2] +1)
        DP[n] = temp
    return DP[number]
    

    

number = int(input())
print(calcul(number))