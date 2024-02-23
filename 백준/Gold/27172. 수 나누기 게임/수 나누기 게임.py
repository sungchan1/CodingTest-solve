from sys import stdin as s
# s = open("input.txt", "r")

n = int(s.readline())

cards = { number : 0 for number in map(int, s.readline().split())}
maximum = max(cards)
for card in cards.keys():
    multiple = 2
    while card * multiple <= maximum:
        if card * multiple in cards:
            cards[card] +=1
            cards[card*multiple] -=1
        multiple +=1

print(" ".join(map(str,cards.values())))