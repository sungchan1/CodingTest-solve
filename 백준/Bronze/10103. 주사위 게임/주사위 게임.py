round_number = int(input())

chang_score = 100
sang_score = 100
for i in range(round_number):
    chang_dice, sang_dice = map(int, input().split())

    if chang_dice == sang_dice:
        pass
    elif chang_dice > sang_dice :
        sang_score -= chang_dice
    else :
        chang_score -= sang_dice
print(chang_score)
print(sang_score)

