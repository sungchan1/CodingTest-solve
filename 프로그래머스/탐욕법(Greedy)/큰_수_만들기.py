def removeNumber(number,index ,k ):
    if k == 0 or len(number) == 1 :        
        return int(number)
    if len (number)  == index+ k:
        return int(number[:index] )
    if index == 0:
        return max(removeNumber(number, index+1, k),removeNumber(number[1:], index , k-1))
    else :
        return max(removeNumber(number, index+1, k),removeNumber(number[:index]+number[index+1:], index , k-1))
        
        
def solution(number, k):
    if len(number) == 1 :
        return 0
    number_list = list(number)     

    answer = removeNumber(number, 0 , k)
    return str(answer)