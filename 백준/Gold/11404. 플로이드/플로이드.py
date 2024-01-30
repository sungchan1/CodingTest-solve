from sys import stdin as s
# s=open("input.txt","rt")

city_number =int(s.readline())
bus_number = int(s.readline())

graph = [[float("inf")] * city_number for city in range(city_number)]

for city in range(city_number):
    graph[city][city] = 0


for bus in range(bus_number):
    start, end, cost = map(int, s.readline().split())
    if graph[start-1][end-1] > cost:
        graph[start-1][end-1] = cost

for m in range(city_number):
    for s in range(city_number):
        for e in range(city_number):
            if graph[s][e] > graph[s][m] + graph[m][e] :
                graph[s][e] = graph[s][m] + graph[m][e]

for start_city in range(city_number):
    for end_city in range(city_number):
        if graph[start_city][end_city] == float("inf"):
            print(0, end=" ")
        else :
            print(graph[start_city][end_city] ,end=" ")
    print()
