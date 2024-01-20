snack_price, snack_number, budge = map(int, input().split())

request = 0
if snack_price *snack_number <= budge:
    request = 0
else :
    request = snack_price * snack_number - budge
print(request)