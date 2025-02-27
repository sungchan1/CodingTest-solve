from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입 차수 (0으로 초기화)

for _ in range(M):
    orders = list(map(int, input().split()))[1:]  
    for i in range(len(orders) - 1):
        # 순서대로 가수들을 연결
        graph[orders[i]].append(orders[i + 1])
        indegree[orders[i + 1]] += 1

q = deque()
result = []

# 진입 차수가 0인 노드를 큐에 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    result.append(current)

    # 연결된 노드들의 진입 차수 감소
    for next_node in graph[current]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

# 만약 결과가 N개가 아니라면, 사이클이 존재한다는 의미
if len(result) != N:
    print(0)
else:
    for node in result:
        print(node)