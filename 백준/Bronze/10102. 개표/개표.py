judge = int(input())
votes = input()

a_count = votes.count("A")
b_count = votes.count("B")
if a_count == b_count :
    result = "Tie"
elif a_count > b_count:
    result= "A"
else:
    result = "B"
print(result)