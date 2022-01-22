import collections


def find_hIndex (collections, h, init=False):
    if isOverH(collections,h) >=0 :
        possibility = max(find_hIndex(collections,h+1)  , h)
        if possibility > 0 :
            return possibility
        else :
            return find_hIndex (collections, h-1)
    else :
        if init :
            return find_hIndex(collections, h-1, init=True)
        else :
            return -1
    
def isOverH(citations, h):
    count = 0
    for quotation, number in citations.items() :
        if quotation >= h :
            count += number
    if count >=h :
        return h
    else :
        return -1
def solution(citations):
    
    # citations.sort()
    if sum(citations) ==0:
        return 0
    collecter = collections.Counter(citations)  
    answer = find_hIndex(collecter,0, init=True)
    return answer


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer