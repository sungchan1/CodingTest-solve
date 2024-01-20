votes_number = int(input())
result = 0
for i in range(votes_number):
    vote = input()
    if vote == "0":
        result -=1
    elif vote == "1":
        result +=1

if result > 0:
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")

