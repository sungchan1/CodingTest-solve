from sys import stdin as s


test_case = int(s.readline())

for test in range(test_case):
    height, width, customer = map(int, s.readline().split())
    floor = str(customer % height) if customer % height != 0 else str(height)
    room_number = "0" + str((customer-1) // height + 1) if ((customer-1)//height + 1) < 10 else str((customer-1)//height + 1)
    room_number = floor + room_number
    print(room_number)