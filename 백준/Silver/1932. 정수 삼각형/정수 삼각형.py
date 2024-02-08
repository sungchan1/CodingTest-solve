from sys import stdin as s
# s = open("input.txt", "r")
layer_number = int(s.readline())

if layer_number == 1:
    print(int(s.readline()))
else:
    triangle_numbers = []
    dp = [[0] * (layer+1) for layer in range(layer_number)]
    
    for layer in range(layer_number):
        triangle_numbers.append(list(map(int, s.readline().split())))

    dp[0][0]= triangle_numbers[0][0]

    for layer in range(layer_number):
        for index in range(layer+1):
            number = triangle_numbers[layer][index]
            if index == 0:
                dp[layer][index] = dp[layer-1][index] + number
            elif index == layer:
                dp[layer][index] = dp[layer-1][index-1] + number
            else:
                dp[layer][index] = max(dp[layer-1][index-1], dp[layer-1][index]) + number
    print(max(dp[-1]))