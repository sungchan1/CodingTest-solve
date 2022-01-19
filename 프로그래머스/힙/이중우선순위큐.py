import heapq

class Double_heap:
    def __init__(self):     
        self.maxheap = list()
        self.minheap = list()
        
    
    def push(self, number):
        heapq.heappush(self.maxheap, -number)
        heapq.heappush(self.minheap, number)
    
    def pop_max(self):
        if self.maxheap and self.minheap :
            max_out = -heapq.heappop(self.maxheap)
            self.minheap.remove(max_out)
            heapq.heapify(self.minheap)

    def pop_min(self):
        if self.maxheap and self.minheap:
            min_out = heapq.heappop(self.minheap)
            self.maxheap.remove(-min_out)
            heapq.heapify(self.maxheap)
        
        
    def return_top(self):
        if self.minheap:
            top_min = heapq.heappop(self.minheap)
            top_max = -heapq.heappop(self.maxheap)
            return top_max, top_min
        else :
            return [0,0]
def solution(operations):
    doubleHeap = Double_heap()
    for operation in operations :
        if operation[0] == "I" :
            doubleHeap.push(int(operation[1:]))
        elif operation == "D -1" :
            doubleHeap.pop_min()
        elif operation == "D 1" :
            doubleHeap.pop_max()
        else :
            print("Error")
            return 
    

    answer = doubleHeap.return_top()
    return answer