from collections import defaultdict

def check_removable(storage, visited, x,y):
    # print(storage,x,y)
    
    if visited[(x,y)]:
        return False
    
    visited[(x,y)] = True
    
    if x == 0 or x == len(storage) -1 or y ==0 or y == len(storage[0]) -1:
        # print(f"탈출 {x} {y} {storage[x][y]}")
        return True
    
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if nx < 0 or nx > len(storage)-1 or y < 0 or y> len(storage[0]) - 1 :
            continue
        
        if storage[nx][ny] == "_":
            if check_removable(storage, visited, nx, ny):
                # print("탈출 성공")
                # print(storage,x,y)
                return True
        
    return False
        
            

def solution(storage, requests):
    answer = len(storage) * len(storage[0])
    # print(f"ANSWER {answer}")
    positions = defaultdict(lambda :defaultdict(list))
    
    for x, line in enumerate(storage):
        for y, box in enumerate(line):
            positions[box][x].append(y)
        
    
    for request in requests:

        box = request[0]
        # print(f"# request {request}")
        if len(request) == 1: # 지게차
            removes = []    
            
            for x, line in positions[request[0]].items():
                for y in line:
                    visited = defaultdict(lambda: False)
                    if storage[x][y] != "_" and check_removable(storage, visited, x, y):
                        removes.append((x,y))
            # print(box, removes)
            
            answer -= len(removes)
            for x,y in removes:
                new_line = list(storage[x])
                new_line[y] = "_"
                storage[x] = ''.join(new_line)


        else: # 크레인
            for x, line in positions[request[0]].items():
                new_line = list(storage[x])
                for y in line:
                    if new_line[y] != "_":
                        new_line[y] = "_"
                        answer -= 1
                storage[x] = ''.join(new_line)
                    
        # print(f"ANSWER {answer}")
                
            
    return answer


