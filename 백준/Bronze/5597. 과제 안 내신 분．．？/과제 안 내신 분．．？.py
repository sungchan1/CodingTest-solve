from sys import stdin as s
students = list(range(1,31))
for i in range(28):
    students.remove(int(s.readline()))
print(students[0])
print(students[1])
