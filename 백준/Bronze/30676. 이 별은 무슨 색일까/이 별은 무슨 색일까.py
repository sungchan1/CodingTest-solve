from sys import stdin as s
from collections import deque
# s = open("input.txt", "r")


freequency = int(s.readline())


if 380 <= freequency <425:
    print("Violet")
elif 425 <= freequency < 450:
    print("Indigo")
elif 450 <= freequency < 495:
    print("Blue")
elif 495 <= freequency < 570:
    print("Green")
elif 570 <= freequency < 590:
    print("Yellow")
elif 590 <= freequency < 620:
    print("Orange")
elif 620 <= freequency <= 780:
    print("Red")

