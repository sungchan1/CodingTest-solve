number = int(input())

divisor = 2
while 1 < number :
    while True:
        if number % divisor == 0 :
            number = number / divisor
            print(divisor)
            break
        else :
            divisor += 1



