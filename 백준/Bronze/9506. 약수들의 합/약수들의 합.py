import math

while True:
    number = int(input())
    if number == -1:
        break

    # 약수들을 저장할 리스트
    divisors = []

    # 약수들을 찾기
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != 1 and i != number // i:
                divisors.append(number // i)

    # 약수들의 합이 주어진 수와 같은지 확인
    if sum(divisors) == number:
        divisors.sort()  # 약수들을 오름차순으로 정렬
        print("{0} = {1}".format(number, " + ".join(map(str, divisors))))
    else:
        print("{0} is NOT perfect.".format(number))