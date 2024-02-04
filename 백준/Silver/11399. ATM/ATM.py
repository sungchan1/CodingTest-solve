from sys import stdin as s

s.readline()

times = list(map(int, s.readline().split()))
times.sort()

result = 0 
person_wait = 0
for wait in times:
    person_wait += wait
    result += person_wait


print(result)
    