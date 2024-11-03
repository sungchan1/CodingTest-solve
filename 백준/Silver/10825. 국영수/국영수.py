from sys import stdin



n = int(input())

students = []
for _ in range(n):
    name, korea, english, math = input().split()
    korea, english, math = int(korea), int(english), int(math)
    students.append((name, korea, english, math))


students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름만 줄 단위로 출력
print(*(student[0] for student in students), sep='\n')
