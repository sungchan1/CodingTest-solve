def borrow_cloth(lost, reserve) :
    if not reserve or not lost :
        return 0

    if lost[0]-1 in reserve and lost[0]+1 in reserve :
        copy_reserve = reserve.copy()
        reserve.remove(lost[0]-1)
        copy_reserve.remove(lost[0]+1)
        return max( borrow_cloth(lost[1:] ,reserve )+1 , borrow_cloth(lost[1:] ,copy_reserve )+1 )
    elif lost[0]-1 in reserve:
        reserve.remove(lost[0]-1)
        return borrow_cloth(lost[1:] ,reserve )+1

    elif lost[0]+1 in reserve :
        reserve.remove(lost[0]+1)
        return borrow_cloth(lost[1:] ,reserve )+1

    else :
        return borrow_cloth(lost[1:] ,reserve )


def solution(n, lost, reserve):
    lost_copy= lost.copy()
    for lost_number in lost_copy:
        if lost_number in reserve:
            reserve.remove(lost_number)
            lost.remove(lost_number)
    print(lost, reserve)
    answer = borrow_cloth(lost,reserve)
    answer += n-len(lost)
    return answer