def solution(clothes):
    
    answer = 1
    case = dict()
    
    for clothe in clothes :
        if clothe[1] in case.keys() :
            case[clothe[1]] +=  1
        else :
            case[clothe[1]] = 1
    
    for catergory, number in case.items():
        answer *= int(number)+1
    
    

    
    return answer-1