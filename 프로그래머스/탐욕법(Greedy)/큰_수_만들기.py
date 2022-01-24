def solution(number, k):
    
    str_list = list(number)
    
    str_length = len(number)-1
    stack_list = ['A'] * (str_length+1) 
    index = 0
    stack_index = 0
    for str_number in str_list :
        if str_number == '0' :
            index +=1
        else :
            break
    if index != 0:
        str_list = str_list[index:]
    stack_list[0] = str_list[0]
    # print("push 1 :", str_list[0])
    index = 1 
    while True :
        if  stack_list[stack_index] >= str_list[index] : # 처음올때 stack_index = 0, index = 1
            stack_list[stack_index+1] = str_list[index]
            # print("push 2 :", str_list[index])
            if index == str_length: #끝까지 왔을 떄
                del str_list[index]
                index = 0
                k -= 1
                if k == 0 :
                    break
                str_length -= 1
                stack_index = -1
                stack_list[0] = str_list[0]
                # print("push 3 :", str_list[index])
            index +=1
            stack_index += 1
        else : # 뒤에 들어온 수가 스택에 수보다 클때
            # print("pop", str_list[index-1], " pre ", stack_list[stack_index], " after ", str_list[index])
            del str_list[index-1]
            k -= 1
            if k == 0 :
                break
            index -=1
            str_length -=1
            stack_index -=1
    return "".join(str_list)