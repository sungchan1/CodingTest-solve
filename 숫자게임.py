def solution(A, B):
    answer = 0
    
    A = sorted(A)
    B = sorted(B)
    B_len = len(B)
    index = 0 
    
    for score_A in A:
        while (index < B_len):
            if B[index] > score_A :
                index +=1 
                answer +=1
                break
            else :
                index +=1
            
    return answer