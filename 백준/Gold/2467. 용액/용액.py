from sys import stdin as s
from collections import deque
# s = open("input.txt", "r")
n = int(s.readline())
ph_waters = deque(map(int, s.readline().split()))
zero_near_ph = float("inf")
zero_near_waters = []
while ph_waters:
    current_ph = ph_waters.popleft()
    start = 0
    mid = 0
    end = len(ph_waters) -1
    while start <= end :
        mid = (end+start) // 2
        mix_ph = current_ph + ph_waters[mid]
        # print("    Current ph: ", current_ph)
        # print("    Target ph : " , ph_waters[mid])
        # print("    MIXED PH  : ", mix_ph)
        # print(" ")
        if zero_near_ph > abs(mix_ph):
            zero_near_ph = abs(mix_ph)
            zero_near_waters = [current_ph, ph_waters[mid]]

        if mix_ph == 0:
            break
        elif mix_ph > 0:
            end = mid -1
        else:
            start = mid +1

    if zero_near_ph == 0:
        break

zero_near_waters.sort()
print(" ".join(map(str, zero_near_waters)))



