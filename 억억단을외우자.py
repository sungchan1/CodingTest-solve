
from collections import deque
def solution(e, starts):
    answer = []
    ukukDan = { i:1 for i in range(1,e+1) } # e까지만 
    starts_dict = {start_point:index for index, start_point in  enumerate(starts)}
    
    for i in range(2,e+1):
        for j in range(1, int(e/i)+1):
            ukukDan[i*j] +=1

    sorted_ukukDan = sorted(ukukDan.items(), key=lambda x : (-x[1],x[0]))
    
    answer = [0] * len(starts)
    start_len = len(starts)
    count = 0
    starts.sort()
    starts = deque(starts)
    for ukukDan_number, ukukDan_count in sorted_ukukDan:
        if starts[0] <= ukukDan_number:
            pop_count = 0
            for start_point in starts :
                if  start_point <= ukukDan_number:
                    answer[starts_dict[start_point]] = ukukDan_number
                    count +=1
                    pop_count +=1
                else :
                    break
            if count == start_len:
                break
            for i in range(pop_count):
                starts.popleft()
        else :
            continue
        
            
        # # if DP_ukukDan and start_number < min(DP_ukukDan.keys()):
        # #     slice_index = max(DP_ukukDan.values())
        # # else:
        # #     slice_index = 0
        #     if sorted_number >= start_number:
        #         answer.append(sorted_number)
        #         # DP_ukukDan[start_number] = index + slice_index
        #         break

    return answer