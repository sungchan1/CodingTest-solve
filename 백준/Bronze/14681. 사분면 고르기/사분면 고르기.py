from sys import stdin as s
x =  int(s.readline())
y =  int(s.readline())

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")

else :
    if y>0:
        print("2")
    else:
        print("3")