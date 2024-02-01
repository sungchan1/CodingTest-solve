from sys import stdin as s
# s=open("input.txt","rt")


n_dict = dict()
s.readline()
numbers = list(map(int, s.readline().split()))
s.readline()
comapares = list(map(int, s.readline().split()))

for number in numbers:
    try:
        n_dict[number] +=1
    except KeyError:
        n_dict[number] = 1

for compare in comapares:
    try:
        print(n_dict[compare], end=" ")
    except KeyError:
        print(0, end=" ")








