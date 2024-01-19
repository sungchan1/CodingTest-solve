score = int(input())
grade = ""

if 90 <= score:
    grade = "A"
elif 80 <= score:
    grade = "B"
elif 70 <= score:
    grade = "C"
elif 60 <= score:
    grade = "D"
else :
    grade = "F"
print(grade)