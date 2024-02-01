from sys import stdin as s
# s=open("input.txt","rt")

test_case = int(s.readline())
q = []
for test in range(test_case):
    age, name = s.readline().split()
    age = int(age)
    q.append([age,name])

q.sort(key=lambda x: x[0])

for  age, name in q:
    print(age, name)
