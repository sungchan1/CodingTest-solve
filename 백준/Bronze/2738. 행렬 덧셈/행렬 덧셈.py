from sys import stdin as s
# s =open("input.txt","r")
n,m = map(int, s.readline().split())

a_list = []
b_list = []
for row in range(n):
    a_list.append(list(map(int, s.readline().split())))

for row in range(n):
    b_list.append(list(map(int, s.readline().split())))

for row in range(n):
    print(" ".join([str(item1+item2) for item1, item2 in zip(a_list[row],b_list[row])]))