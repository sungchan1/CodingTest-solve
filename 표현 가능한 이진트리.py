import math
def DFS(binary, parent):
    # print(binary, parent)
    if len(binary) == 1:
        if parent == 0 and int(binary) == 1:
            # print("return 0 " )
            return 0
        else :
            return 1
    mid_index = math.floor(len(binary)/2)
    root = int(binary[mid_index])
    if parent == 0 and root == 1:
        return 0
    left_node = binary[:mid_index]
    right_node = binary[mid_index+1:]
    return min (DFS(left_node, root) ,DFS(right_node, root))
    
def solution(numbers):
    answer = []
    height = 0
    for number in numbers :
        binary_number = bin(number)[2:]
        log2_binary_len = math.log2(len(binary_number)+1)
        if log2_binary_len == int(log2_binary_len) :
            height = log2_binary_len
        else :
            height =  math.ceil(log2_binary_len)
            binary_number = '0' * (2**height-1 - len(binary_number)) +binary_number
        mid_index = math.floor(len(binary_number)/2)
        # print(binary_number)
        answer.append(DFS(binary_number, int(binary_number[mid_index])))
    return answer