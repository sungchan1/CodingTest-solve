from sys import stdin as s
# s =open("input.txt","r")
result = ""
for char in s.readline().rstrip():
    if char.islower():
        result += char.upper()
    else:
        result += char.lower()
print(result)