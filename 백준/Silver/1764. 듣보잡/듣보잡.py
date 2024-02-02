from sys import stdin as s
# s = open("input.txt", "r")

n,m = map(int, s.readline().split())

no_listen_people = []
no_see_people = []
for no_listen in range(n):
    no_listen_people.append(s.readline().rstrip())


for no_see in range(m):
    no_see_people.append(s.readline().rstrip())
no_listen_people = set(no_listen_people)
no_see_people = set(no_see_people)

result = sorted(list(no_listen_people & no_see_people))
print(len(result))
print("\n".join(result))


