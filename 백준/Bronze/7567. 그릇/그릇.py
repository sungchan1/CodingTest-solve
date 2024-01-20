plates  = input()
height = 10
gap = 5
result = 0

for index in range(len(plates)):
    if index == 0:
        result += height
    elif plates[index-1] == plates[index] :
        result += gap
    else :
        result += height
print(result)
