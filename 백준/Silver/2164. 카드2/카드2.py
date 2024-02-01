from sys import stdin as s
from collections import deque
# s=open("input.txt","rt")

card_number = int(s.readline())
cards = deque(list(range(1,card_number+1)))

while len(cards) > 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards[0])


