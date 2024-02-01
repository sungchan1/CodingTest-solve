from sys import stdin as s
from collections import deque
# s=open("input.txt","rt")

test_case = int(s.readline())
q = deque([])
for test in range(test_case):
    command = s.readline().split()
    if len(command) == 1:
        command = command[0].strip()
    elif len(command) == 2:
        command, item = command[0], int(command[1])

    match command:
        case "push":
            q.append(item)
        case "pop":
            if q:
                print(q.pop())
            else:
                print("-1")
        case "size":
            print(len(q))
        case "empty":
            if q:
                print("0")
            else:
                print("1")
        case "top":
            if q:
                print(q[-1])
            else:
                print("-1")




