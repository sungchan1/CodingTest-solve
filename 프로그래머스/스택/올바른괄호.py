def solution(s):
    
    # answer = True
    # stack = []
    # for bracket in s :
    #     if bracket == '(' :
    #         stack.append(1)
    #     elif bracket == ')' and  stack :
    #         stack.pop(0)
    #     else :
    #         return False
    # if stack:
    #     return False
    # else:
    #     return True
    
    answer = True
    stack = 0
    for bracket in s :
        if bracket == '(' :
            stack += 1
        elif bracket == ')' :
            stack -= 1
            if stack < 0 :
                return False
            
    if stack  == 0 :
        return True
    else:
        return False