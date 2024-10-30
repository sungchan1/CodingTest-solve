

number = list(map(int, list(input())))

# print(number)
number.sort(key=(lambda x: -x))
#
#
print("".join(list(map(str, number))))