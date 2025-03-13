from collections import deque

def bfs(start, graph):
    visited = [-1] * len(graph)
    queue = deque([(start, 0)])
    visited[start] = 0
    farthest_node = start
    max_distance = 0

    while queue:
        node, dist = queue.popleft()

        if dist > max_distance:
            max_distance = dist
            farthest_node = node

        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = dist + weight
                queue.append((next_node, dist + weight))

    return farthest_node, max_distance

def find_diameter(V, edges):
    graph = [[] for _ in range(V + 1)]
    
    for edge in edges:
        u = edge[0]
        for i in range(1, len(edge) - 1, 2):
            v, w = edge[i], edge[i + 1]
            graph[u].append((v, w))
    
    farthest_node_from_start, _ = bfs(1, graph)
    
    _, diameter = bfs(farthest_node_from_start, graph)
    
    return diameter

V = int(input()) 
edges = []

for _ in range(V):
    edge_info = list(map(int, input().split()))
    edges.append(edge_info)

print(find_diameter(V, edges))