from sys import stdin as s
# s = open("input.txt", "r")

n = int(s.readline())
result = 0
first_vertex = []
pre_vertex = []

for vertex in range(n):
    x,y = map(float, s.readline().split())
    if vertex == 0:
        first_vertex = [x,y]
    else:
        result += (y*pre_vertex[0] - x*pre_vertex[1]) * 0.5
    pre_vertex = [x,y]

    if vertex == (n-1):
        result += (first_vertex[1]*pre_vertex[0] - first_vertex[0]*pre_vertex[1]) * 0.5
print(round(abs(result), 2))
