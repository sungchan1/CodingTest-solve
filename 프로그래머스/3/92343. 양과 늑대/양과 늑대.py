
def solution(info, edges):
    fail = -1
    SHEEP_NODE = 0
    WOLF_NODE = 1
    
    visited = [False] * len(info)

    def dfs(sheep, wolf):
        if sheep <= wolf:
            return 0
    
        max_sheep = sheep
        
        for start, end in edges:
            if visited[start] and not visited[end]:
                visited[end] = True


                if info[end] == SHEEP_NODE:
                    max_sheep = max(max_sheep, dfs(sheep+1, wolf))
                else:
                    max_sheep = max(max_sheep, dfs(sheep, wolf+1))

                visited[end] = False
        return max_sheep

    
    visited[0] = True
    return dfs(1,0)



