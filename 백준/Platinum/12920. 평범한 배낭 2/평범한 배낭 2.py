from sys import stdin

# 입력 처리
N, M = map(int, input().split())  # N: 물건 종류, M: 최대 무게

items = []

# 이진 분할로 아이템 처리
for _ in range(N):
    V, C, K = map(int, stdin.readline().split())
    count = 1
    while K > 0:
        take = min(count, K)  # K가 부족하면 남은 만큼만 가져옴
        items.append((V * take, C * take))  # 무게와 가치를 take만큼 추가
        K -= take
        count *= 2

# DP 메모이제이션
dp = [0] * (M + 1)

for weight, value in items:
    for w in range(M, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[-1])
