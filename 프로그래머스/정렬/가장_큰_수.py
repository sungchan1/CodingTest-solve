def find_number (number, order):
    
    if len(str(number)) > order :
        return_number = int(str(number)[order])
    else :
        return_number= find_number(number, order -1)

    return return_number 
def solution(numbers):
    answer = ''
    
    if sum(numbers) == 0:
        return 0
    
    ordered_list = sorted(numbers , key = lambda x : ( find_number(x,0), find_number(x,1),find_number(x,2),find_number(x,3), -x)  )
        # front_number(x,0), front_number(x,1), front_number(x,2), front_number(x,3), front_number(x,4),front_number(x,5
    print(ordered_list)    
    
    ordered_list.reverse()
    print(ordered_list)    


    # print(ordered_list)
    for x in ordered_list :
        answer += str(x)
    return answer


