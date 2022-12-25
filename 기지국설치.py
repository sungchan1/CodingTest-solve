import math

def solution(n, stations, w):
    w_range = w*2+1
    answer = 0
    outOfRange = 1
    
    for station in stations:
        effective_left = station - w
        if effective_left <= 1: # 유효범위 왼쪽
            outOfRange = station + w + 1 # 유효범위 오른쪾 바깥
        else:
            distance = effective_left-outOfRange
            answer += math.ceil(distance/w_range)
            outOfRange = station + w + 1
            
    if station + w  < n:
        outOfRange = station + w
        distance = n -outOfRange
        answer += math.ceil(distance/w_range)

    return answer

