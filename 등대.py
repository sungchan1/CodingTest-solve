def solution(n, lighthouse):
    from collections import defaultdict
    import heapq
    
    graph = defaultdict(list)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    
    def dijkstra(start):
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            dist, current = heapq.heappop(heap)
            if visited[current]:
                continue
            visited[current] = True
            for neighbor in graph[current]:
                new_distance = dist + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
                    
    dijkstra(1)
    dijkstra(distances.index(max(distances)))
    
    return max(distances)
