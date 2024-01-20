hour, minute = map(int, input().split())
gap = 45

minute = minute - gap

if minute < 0:
    minute += 60
    hour -= 1

if hour < 0:
    hour += 24

print(hour, minute)