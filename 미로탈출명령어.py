from collections import deque

# def solution(n, m, x, y, r, c, k):
#     answer = ''
#     q = deque([(x,y,"", 0)])
#     while q:
#         pos_x, pos_y, path, count = q.popleft()
#         print(pos_x, pos_y, path, count)
        
#         if count == k :
#             if pos_x == r and pos_y == c :
#                 # print(pos_x, pos_y, path, count)
#                 answer = path
#                 return answer
#             else :
#                 continue
#         if  abs(r-pos_x) + abs(c-pos_y) > k -count :
#             print("가지치기 ",pos_x, pos_y, path, count )
#             continue
#         if pos_x < n : # down
#             q.append((pos_x+1,pos_y,path+"d", count+1))
#         if pos_y > 1 : # left 
#             q.append((pos_x,pos_y-1,path+"l", count+1))
#         if pos_y < m : # right
#             q.append((pos_x,pos_y+1,path+"r", count+1))
#         if pos_x > 1 : # up
#             q.append((pos_x-1,pos_y,path+"u", count+1))
            
#     answer = "impossible"
#     return answer

def solution(n, m, x, y, r, c, k):
    answer = ''
    dist = abs(x-r)+abs(y-c)
    k -= dist
    if k < 0 or k%2 != 0:
        return "impossible"
    
    direction = {'d':0, 'l':0, 'r':0, 'u':0}
    if x > r:
        direction['u'] += x-r
    else:
        direction['d'] += r-x
    if y > c:
        direction['l'] += y-c
    else:
        direction['r'] += c-y
        
    answer += 'd'*direction['d']
    d = min(int(k/2), n-(x+direction['d']))
    answer += 'd'*d
    direction['u'] += d
    k -= 2*d
    
    answer += 'l'*direction['l']
    l = min(int(k/2), y-direction['l']-1)
    answer += 'l'*l
    direction['r'] += l
    k -= 2*l
    
    answer += 'rl'*int(k/2)
    answer += 'r'*direction['r']
    answer += 'u'*direction['u']
    return answer