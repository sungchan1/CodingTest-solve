from sys import stdin as s
# s = open("input.txt", "r")
test_case = int(s.readline())
for test in range(test_case):
    sticker_length = int(s.readline())
    stickers = []
    stickers.append(list(map(int, s.readline().split())))
    stickers.append(list(map(int, s.readline().split())))
    dp = [[0] * 2 for index in range(sticker_length+1)]

    dp[0][0] = 0
    dp[0][1] = 0
    dp[1][0] = stickers[0][0]
    dp[1][1] = stickers[1][0]
    for index in range(2, sticker_length+1):
        dp[index][0] = max(dp[index-2][1], dp[index-1][1]) + stickers[0][index-1]
        dp[index][1] = max(dp[index - 2][0], dp[index - 1][0]) + stickers[1][index-1]
    print(max(dp[-1]))

