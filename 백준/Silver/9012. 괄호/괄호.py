from sys import stdin as s
# s=open("input.txt","rt")

test_number = int(s.readline())


for test in range(test_number):
    string = s.readline()
    count = 0
    for character in string:
        if character == "(":
            count +=1
        elif character == ")":
            count -=1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")