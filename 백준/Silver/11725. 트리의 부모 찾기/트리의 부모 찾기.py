from collections import deque
from sys import stdin as s
# s = open("input.txt", "r")
node_number = int(s.readline())
nodes = [ [] for _ in range(node_number)]
for test in range(node_number-1):
    node_1, node_2 = map(int, s.readline().split())
    nodes[node_1-1].append(node_2-1)
    nodes[node_2-1].append(node_1-1)

result = [-1] * node_number
visited = [False] * node_number
q = deque([])
q.append(0)

while q:
    node = q.popleft()
    visited[node] = True
    for connected_node in nodes[node]:
        if not visited[connected_node] :
            result[connected_node] = node+1
            q.append(connected_node)
print("\n".join(map(str,result[1:])))
