def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    prefix_sum = [[0] * (m+1) for _ in range(n+1)]
    
    # 스킬 적용
    for action in skill:
        _type, r1, c1, r2, c2, degree = action
        effect = degree if _type == 2 else -degree
        
        prefix_sum[r1][c1] += effect
        prefix_sum[r2+1][c2+1] += effect
        
        prefix_sum[r1][c2+1] -= effect
        prefix_sum[r2+1][c1] -= effect
        
    # 누적합 - 가로 합
    for r in range(n):
        for c in range(1, m+1):
            prefix_sum[r][c] += prefix_sum[r][c-1] 
            
    # 누적합 - 세로 합
    for c in range(m):
        for r in range(1,n+1):
            prefix_sum[r][c] += prefix_sum[r-1][c] 
        

    for r in range(n):
        for c in range(m):
            if board[r][c] + prefix_sum[r][c] > 0 :
                answer +=1
            
    return answer