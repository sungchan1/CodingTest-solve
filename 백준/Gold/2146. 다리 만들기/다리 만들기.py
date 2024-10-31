from sys import stdin
from collections import deque, defaultdict

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col, index):
    island = islands[index]
    q = deque([(row, col)])

    while q:
        r, c = q.popleft()

        if (r, c) in island:
            continue

        island.add((r, c))

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= size or nc < 0 or nc >= size:
                continue

            if (nr, nc) in island:
                continue

            elif world[nr][nc] == 0:
                continue

            q.append((nr, nc))

    total_island.update(island)


size = int(input())

islands = defaultdict(set)
total_island = set()

world = [
    list(map(int, input().split()))
    for _ in range(size)
]

# 섬을 찾고 색인 처리
island_count = 0
for i in range(size):
    for j in range(size):
        if world[i][j] == 1 and (i, j) not in total_island:
            bfs(i, j, island_count)
            island_count += 1

bridge = float("inf")

# 각 섬에서 다리 놓기 시도
for i in range(island_count):
    island = islands[i]
    visited = [[False] * size for _ in range(size)]
    q = deque([(r, c, 0) for r, c in island])  # 시작점 큐에 거리 0으로 넣기

    while q:
        r, c, distance = q.popleft()

        if visited[r][c]:
            continue

        # 다른 섬에 도달하면 다리의 길이를 갱신
        if world[r][c] == 1 and (r, c) not in island:
            bridge = min(bridge, distance)
            break

        visited[r][c] = True

        # 거리 1 증가하며 인접한 좌표 탐색
        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]

            if 0 <= nr < size and 0 <= nc < size and not visited[nr][nc]:
                q.append((nr, nc, distance + 1))

print(bridge-1)
