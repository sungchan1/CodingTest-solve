def check_array(arr_a, arr_b):
    for i in reversed(range(11)):
        if arr_a[i] == arr_b[i] :
            pass
        elif arr_a[i] > arr_b[i]:
            return arr_a
        else :
            return arr_b


def get_score(uppeach, ryan):
    uppeach_score = 0
    ryan_score = 0 
    for i in range(11):
        if uppeach[i] == 0 and ryan[i] == 0:
            pass
        elif ryan[i] > uppeach[i] :
            ryan_score += (10 -i)
        else :
            uppeach_score += (10 -i)
    score_gap = ryan_score-uppeach_score
    if score_gap > 0 :
        return score_gap, ryan
    else :
        return -1, [-1]
            
def dfs(n, uppeach_shot, index, ryan_shot):
    # 탈출 조건
    if n == 0:
        return get_score(uppeach_shot,ryan_shot)
    elif index == 10:
        # 다 때려 부어
        ryan_shot[10] += n
        return get_score(uppeach_shot,ryan_shot)
    uppeach_hit = uppeach_shot[index]
    # 이번꺼 패스
    pass_ryan = ryan_shot[:]
    pass_ryan_score, pass_ryan = dfs(n, uppeach_shot, index+1, pass_ryan)
     # 이번꺼 쟁취
    if n > uppeach_hit:
        get_ryan = ryan_shot[:]
        get_ryan[index] = uppeach_hit+1
        get_ryan_score, get_ryan= dfs(n-(uppeach_hit+1), uppeach_shot, index+1, get_ryan)
        
        if pass_ryan_score >get_ryan_score:
            return pass_ryan_score, pass_ryan
        elif  get_ryan_score >  pass_ryan_score :
            return get_ryan_score, get_ryan
        else :
            if get_ryan_score == -1:
                return get_ryan_score, get_ryan
            return get_ryan_score, check_array(pass_ryan, get_ryan)
    return pass_ryan_score, pass_ryan
        

def solution(n, info):
    ryan_shot = [0 for _ in range(11)]
    index = 0
    score, answer = dfs(n, info, index, ryan_shot)
    return answer