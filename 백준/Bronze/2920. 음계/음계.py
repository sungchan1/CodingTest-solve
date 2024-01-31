da_long = "12345678"

song = input().replace(" ","")

if song == da_long:
    print("ascending")
elif song == da_long[::-1]:
    print("descending")
else:
    print("mixed")