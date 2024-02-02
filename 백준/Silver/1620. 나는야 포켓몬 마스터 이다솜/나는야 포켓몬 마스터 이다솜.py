from sys import stdin as s
#s = open("input.txt", "r")

n,m = map(int, s.readline().split())

poketmon_list = []
poketmon_dict = {}
for index, pk in enumerate(range(n)):
    name = s.readline().rstrip()
    poketmon_list.append(name)
    poketmon_dict[name] = index

for test in range(m):
    search: str = s.readline().rstrip()
    if search.isnumeric():
        print(poketmon_list[int(search)-1])
    else:
        print(poketmon_dict[search]+1)





