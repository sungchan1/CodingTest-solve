def solution(n, s):

    if s < n :
        return [-1]
    
    answer = [ int(s/n) for i in range(n)]

    indexs = len(answer)-1

    for i in range(s - sum(answer)):
        answer[indexs] += 1
        indexs -= 1

    return answer