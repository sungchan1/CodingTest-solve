import math, itertools

def isPrimeNumer(number):
    
    if number == 1 or number == 0 :
        return False
    elif number == 2:
        return True
    
    for i in range(2, int(math.sqrt(number))+1) :
        if number % i == 0:
            return False

    return True

def toInt (strList):
    result = ""
    for st in strList:
        result += st
    return int(result)
        
        
def solution(numbers):
    
    answer = 0
    answer_list = list()
    for i in range(len(numbers)) :
        permutations_list = list(map(toInt, (set(itertools.permutations(numbers, i+1)))))
        for number in permutations_list:
            if  not number in answer_list and isPrimeNumer(number):
                answer_list.append(number)
                answer +=1
    return answer