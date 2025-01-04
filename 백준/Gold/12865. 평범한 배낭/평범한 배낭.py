N, K = map(int, input().split())

items = [
    list(map(int, input().split()))
    for _ in range(N)
]

dp = [0] * (K + 1)  # 1차원 DP 배열

for weight, value in items:
    # 무게를 K부터 weight까지 거꾸로 탐색 (값이 덮어쓰이지 않도록)
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[K])