def solution(n, k):
    answer = 0
    
    # 소수 세팅
    primes = [True] * (1_000_000+1)
    primes[0] = primes[1] = False
    
    for leap in range(2,1000+1):
        for i in range(leap*2, 1_000_000+1, leap):
            primes[i] = False
    
    # k 진수 구하기
    k_system = ""
    while n > 0:    
        k_system = str(n%k) + k_system
        n = n // k
    
    
    # 0 으로 스플릿 하기
    numbers = [ int(num) for num in k_system.split("0") if num ]
    
    # 갯수 세기 
    
    # 소수 판별
    def is_prime(x):
        if x < len(primes):
            return primes[x]
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    for number in numbers:
        if is_prime(number):
            answer +=1
    
    
    return answer