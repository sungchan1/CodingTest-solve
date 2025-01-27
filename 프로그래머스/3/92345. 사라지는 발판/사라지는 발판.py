
A_TURN = True
B_TURN = False

BROKEN = False
EXIST = True
    
    
def get_status(board, loc):
    return board[loc[0]][loc[1]]

def get_movable(board, loc):
    
    position = []
    
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    
    for i in range(4):
        nr, nc = loc[0] + dr[i], loc[1] + dc[i]
        if nr < 0 or nc < 0  or nr >= len(board) or nc >= len(board[0]):
            continue
        
        if board[nr][nc] == EXIST:
            position.append([nr, nc])
    
    return position


def simulation(board, aloc, bloc, count):    
    loc = aloc if count % 2 == 0 else bloc 
    turn =  A_TURN if count % 2 == 0 else B_TURN 

    # 현재 발판이 사라진 경우
    if get_status(board, loc) == BROKEN:
        return not turn, count


    # 움직일 곳이 없는 경우
    movable_positions = get_movable(board, loc)
    if not movable_positions:
        return not turn, count


    min_count = float("INF")
    max_count = -float("INF")
    win = not turn

    # 움직일 경우
    board[loc[0]][loc[1]] = BROKEN

    for next_pos in movable_positions:
        if turn == A_TURN:
            result, _count = simulation(board, next_pos, bloc, count+1)
        else:
            result, _count = simulation(board, aloc, next_pos, count+1)

        if result == turn : # 다음 턴 플레이가 무조건 지는경우
            win = turn
            min_count = min(min_count, _count)
        else:
            max_count = max(max_count, _count)

    board[loc[0]][loc[1]] = EXIST

    result_count = min_count if win == turn else max_count

    return win, result_count

    
def solution(board, aloc, bloc):
    answer = -1
    
    return simulation(board, aloc, bloc, 0)[1]
