import math

while True:
    number = int(input())
    if number == -1:
        break
    result = 0
    divisor = set()
    for count in range(1, int(math.sqrt(number)+1)):
        if number % count == 0:
            divisor.add(count)
            divisor.add(int(number / count))
    divisor = list(divisor)
    divisor.sort()
    if sum(divisor) == number *2 :
        divisor.remove(number)
        print("{0} = {1}".format(number, " + ".join(map(str, divisor))))
    else :
        print("{0} is NOT perfect.".format(number))


