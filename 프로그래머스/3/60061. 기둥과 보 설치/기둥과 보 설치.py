def can_build(build_set, item):
    x,y,build_type = item
    if build_type == 0 : # 기둥
        # 바닥 or 기둥 위 or 보 끝 위
        if y == 0 or ((x,y-1,0) in build_set) or ((x,y,1) in build_set) or \
        ((x-1,y,1) in build_set):
            return True
    else : # 보
        # 기둥 위 or 양쪽 끝이 보
        if ((x,y-1,0) in build_set) or ((x+1,y-1,0) in build_set) or\
        (((x-1,y,1) in build_set) and ((x+1,y,1) in build_set)):
            return True
    return False 
        
        
def is_valid(build_set):
    for build_item in build_set:
        if not can_build(build_set,build_item):
            return False
    return True
        
        
def solution(n, build_frame):
    answer = [] # [[x,y,a]0 은 기둥 1은 보 , 순서는 x, y, 기둥->보
    build_set = set() 
    for build in build_frame :
        x,y,build_type,action = build
        item = (x,y,build_type)
        if action == 0: # 삭제
            build_set.remove(item)
            if not is_valid(build_set):
                build_set.add(item)
        else : # 설치
            if can_build(build_set,item):
                build_set.add(item) 
    answer = list(build_set)
    answer = sorted(answer, key = lambda x : (x[0], x[1], x[2])) 
    return answer