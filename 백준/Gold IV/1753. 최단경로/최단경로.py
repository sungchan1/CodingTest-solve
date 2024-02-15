import heapq
from sys import stdin as s
# s = open("input.txt", "r")

vertex_number, edge_number = map(int, s.readline().split())
start_vertex = int(s.readline())-1

graph = [ dict() for _ in range(vertex_number)]
q = []
for edge in range(edge_number):
    start, end, weight = map(int, s.readline().split())
    start -= 1
    end -=1
    if not (end in graph[start]):
        graph[start][end] = weight
    elif graph[start][end] > weight:
        graph[start][end] = weight
    else:
        pass



heapq.heappush(q, (0, start_vertex))
distances = [float("inf")] * vertex_number
distances[start_vertex] = 0

while q:
    distance, vertex = heapq.heappop(q)
    if distance > distances[vertex]:
        continue

    for next_vertex, weight in graph[vertex].items():
        if weight < float("inf"):
            cost = distance + weight
            if distances[next_vertex] > cost:
                distances[next_vertex] = cost
                heapq.heappush(q, (cost, next_vertex))


for distance in distances:
    if distance == float("inf") :
        print ("INF")
    else:
        print(distance)

