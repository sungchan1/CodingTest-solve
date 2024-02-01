from sys import stdin as s
# s=open("input.txt","rt")



test_number = int(s.readline())
points = list()

for test in range(test_number):
    points.append(list(map(int, s.readline().split())))
points.sort(key=lambda x:(x[0], x[1]))

for point in points:
    print(point[0], point[1])
