
while True:
    boys, girls = map(int, input().split())
    if boys * girls == 0:
        break
    else:
        print(boys+ girls)
