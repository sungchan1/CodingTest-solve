MOD = 1000000007
N = 8

# 입력 받기
D = int(input())

# 초기 인접 행렬 설정
adj_matrix = {
    1: [
        [0, 1, 0, 0, 0, 0, 0, 1],  # 정보과학관
        [1, 0, 1, 0, 0, 0, 0, 1],  # 전산관
        [0, 1, 0, 1, 0, 0, 1, 1],  # 미래관
        [0, 0, 1, 0, 1, 0, 1, 0],  # 신양관
        [0, 0, 0, 1, 0, 1, 0, 0],  # 한경직기념관
        [0, 0, 0, 0, 1, 0, 1, 0],  # 진리관
        [0, 0, 1, 1, 0, 1, 0, 1],  # 학생회관
        [1, 1, 1, 0, 0, 0, 1, 0],  # 형남공학관
    ]
}


def count_paths(d, start, to):
    if d <= 1:
        return adj_matrix[d][start][to]

    if d not in adj_matrix:
        adj_matrix[d] = [[0 for _ in range(N)] for _ in range(N)]
    elif adj_matrix[d][start][to] != 0:
        return adj_matrix[d][start][to]

    half = d // 2
    other = half + 1 if d % 2 else half

    for k in range(N):
        adj_matrix[d][start][to] += count_paths(half, start, k) * count_paths(other, k, to)
        adj_matrix[d][start][to] %= MOD

    return adj_matrix[d][start][to]


print(count_paths(D, 0, 0))
