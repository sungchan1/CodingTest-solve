import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 : 
        min_1 = heapq.heappop(scoville)
        if min_1 >= K :
            return answer
        
        else :
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1+min_2*2)   
            answer += 1
    if heapq.heappop(scoville) >= K :
        return answer
    else :
        return -1