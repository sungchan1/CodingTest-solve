test_number = int(input())

max = 0
for test in range(test_number):
    cube_eyes = sorted(list(map(int, input().split())))
    differ_eyes_number = len(set(cube_eyes))
    reword = 0
    if differ_eyes_number == 1:
        reword = 10000 + cube_eyes[0] * 1000
    elif differ_eyes_number == 2:
        reword = 1000 + cube_eyes[1] * 100

    else:
        reword = cube_eyes[2] * 100

    if max < reword:
        max =reword

print(max)





