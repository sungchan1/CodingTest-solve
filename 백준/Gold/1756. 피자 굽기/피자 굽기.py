D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizzas = list(map(int, input().split()))


for i in range(1, D):
    # 밑에 있는 게 더 커봐야, 위에서 내리는 거라 안 들어감
    if oven[i - 1] < oven[i]:
        oven[i] = oven[i - 1]

layer = D - 1
result = -1


for pizza in pizzas:
    while layer >= 0 and oven[layer] < pizza:
        layer -= 1

    if layer < 0:
        result = -1
        break

    # 피자 놓음
    result = layer
    layer -= 1


print(result + 1)
