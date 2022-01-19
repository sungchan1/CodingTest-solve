
def solution(array, commands):
    answer = []
    for [start, end, number] in commands :
        slice_array = array[start-1:end]
        slice_array.sort()
        answer.append(slice_array[number -1])
    return answer



def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
