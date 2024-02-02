from sys import stdin as s
# s = open("input.txt", "r")

test_number = int(s.readline())
my_set = set()
for test in range(test_number):
    commands = s.readline().split(" ")
    if len(commands) > 1:
        command, number = commands[0], int(commands[1])
    else :
        command = commands[0].rstrip()
    match command:
        case "add":
            my_set.add(number)
        case "remove":
            if number in my_set:
                my_set.remove(number)
        case "check":
            if number in my_set:
                print("1")
            else:
                print("0")
        case "toggle":
            if number in my_set:
                my_set.remove(number)
            else:
                my_set.add(number)
        case "all":
            my_set = set(list(range(1,21)))
        case "empty":
            my_set = set()





