def solution(sticker):
    size = len(sticker)
    if size == 1:
        return sticker[0]
    
    stick_array = [[0 for _ in range(size)] for _ in range(2)]
    stick_array[0][0] = sticker[0]
    stick_array[0][1] = sticker[0]
    stick_array[1][1] = sticker[1]
    
    for i in range(2, size-1): 
        stick_array[0][i] = max(stick_array[0][i-2]+sticker[i], stick_array[0][i-1])
    for i in range(2, size): 
        stick_array[1][i] = max(stick_array[1][i-2]+sticker[i], stick_array[1][i-1])
    answer = max(stick_array[0][size-2], table[1][size-1])
    return answer