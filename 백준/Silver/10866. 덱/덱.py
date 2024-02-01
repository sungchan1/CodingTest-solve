from collections import deque
from sys import stdin as s
# s=open("input.txt","rt")

test_case =int(s.readline())
q = deque([])
for test in range(test_case):
    command = s.readline().split(" ")
    if len(command) > 1:
        command, option = command[0], int(command[1])
    else:
        command = str(command[0]).strip()
    match command:
        case "push_front":
            q.appendleft(option)
        case "push_back":
            q.append(option)
        case "pop_front":
            if q:
                print(q.popleft())
            else:
                print("-1")
        case "pop_back":
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
        case "front":
            if q:
                print(q[0])
            else:
                print("-1")
        case "back":
            if q:
                print(q[-1])
            else:
                print("-1")
    # print(command, q)
    # print()



