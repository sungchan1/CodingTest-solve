# 홀수 = 홀홀홀
# 홀수 = 홀짞짞
import itertools, math

def isPrime_odd(numbers) :
    number = sum(numbers)
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0 :
            return False
    return True


def isPrime_even(evens, odd_number) :
    number = sum(evens) + odd_number
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0 :
            return False
    return True

def solution(nums):
    odd_list  = [num for num in nums if  num %2 == 1 ]
    even_list = [num for num in nums if  num %2 == 0 ]
    answer = 0
    
    # 홀수 = 홀홀홀 
    if len(odd_list) > 2 :
        triple_odds = itertools.combinations(odd_list, 3)
        for triple_odd in triple_odds:
            if isPrime_odd(triple_odd) :
                answer += 1
    # 홀수 = 홀짝짝
    
    if len(even_list) > 1 and len (odd_list) > 0:
        for odd_number in odd_list:
            double_evens = itertools.combinations(even_list, 2)
            for evens in double_evens :
                if isPrime_even(evens, odd_number) :
                    answer += 1
    return answer

if __name__ == '__main__': 
    print( solution ([1,2,3,4,5,6,7,8,9]))
    