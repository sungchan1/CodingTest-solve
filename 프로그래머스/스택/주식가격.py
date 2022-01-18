def solution(prices):
    answer = [0] * len(prices)
    days= 0
    prices_history = list()
    for current_price in prices :
        while True :
            if prices_history and prices_history[-1][1] > current_price:
                out = prices_history.pop(-1)
                answer[out[0]] = days - out[0]
            else :
                prices_history.append([days , current_price])
                break
        days +=1
    days -=1
    for result in prices_history :
        answer[result[0]] = days - result[0]

    return answer