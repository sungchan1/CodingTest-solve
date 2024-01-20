cube_eyes = sorted(list(map(int, input().split())))
cube_eyes_set = set(cube_eyes)
cube_set_len = len(cube_eyes_set)
result = 0
if cube_set_len == 1:
    result = 10000 + cube_eyes[0] * 1000
elif cube_set_len == 2:
    result = 1000 + cube_eyes[1] * 100
else:
    result = cube_eyes[2] * 100

print(result)