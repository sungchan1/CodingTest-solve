from sys import stdin as s
# s = open("input.txt", "r")

n = int(s.readline())

cards = { number : 0 for number in map(int, s.readline().split())}
maximum = 1000000
for card in cards.keys():
    target = card * 2
    while target <= maximum:
        if target in cards:
            cards[card] +=1
            cards[target] -=1
        target += card

print(*cards.values())