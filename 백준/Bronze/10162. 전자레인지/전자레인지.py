total_time = int(input())

button_a = 300
button_b = 60
button_c = 10

clicks = list()

if total_time % button_c != 0 :
    print("-1")
else :
    clicks.append(total_time // button_a)
    total_time %= button_a
    clicks.append(total_time // button_b)
    total_time %= button_b
    clicks.append(total_time // button_c)
    print(" ".join(map(str, clicks)))
