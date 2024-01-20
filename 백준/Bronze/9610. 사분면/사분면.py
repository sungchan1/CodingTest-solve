test_number = int(input())

q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for i in range(test_number):
    x, y = map(int, input().split())

    if x * y == 0:
        axis += 1
    elif x < 0:
        if y < 0:
            q3 += 1
        else :
            q2 += 1
    else:
        if y< 0:
            q4 +=1
        else:
            q1 +=1


print("Q1: {0}".format(q1))
print("Q2: {0}".format(q2))
print("Q3: {0}".format(q3))
print("Q4: {0}".format(q4))
print("AXIS: {0}".format(axis))
