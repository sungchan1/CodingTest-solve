
N, K = map(int, input().split())


items = [
	list(map(int, input().split()))
	for i in range(N)
]


dp = [ [0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
	for w in range(1,K+1):
		weight = items[i-1][0]
		value = items[i-1][1]

		if weight > w:
			dp[i][w] = dp[i-1][w]
		else:
			dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)


print(dp[N][K])