from collections import deque
from sys import stdin as s

# s = open("input.txt", "r")

computer_number = int(s.readline())
network_node = int(s.readline())
networks = [[False] * computer_number for computer in range(computer_number)]
visited = [False for computer in range(computer_number)]
result = []

for i in range(network_node):
    com1, com2 = map(int, s.readline().split())
    networks[com1-1][com2-1] = True
    networks[com2-1][com1-1] = True
q = deque([])
q.append(0)
visited[0] = True

while q:
    computer = q.popleft()
    result.append(computer)
    for index, connect in enumerate(networks[computer]):
        if connect and visited[index] == False:
            q.append(index)
            visited[index] = True

print(len(result)-1)














