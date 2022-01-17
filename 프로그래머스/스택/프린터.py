class Document : 
    def __init__(self, name, priority) :
        self.name = name
        self.priority = priority
        
def solution(priorities, location):
    
    prints = [Document(name, priority) for name,priority in zip(range(len(priorities)), priorities )]
    
    exit_number = 1
    while prints :
        wait_list =  [document.priority for document in prints ]
        first = prints.pop(0) 
        if first.priority == max(wait_list) : 
            if location == first.name:
                return exit_number
            else :
                exit_number += 1
        else :
            prints.append(first)
            
