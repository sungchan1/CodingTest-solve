def solution(money, costs):
    answer = 0

    cost_value = dict()
    coins = [ "1","5","10",	"50",	"100"	,"500"]

    for coin, cost in zip (coins, costs):
        cost_value[coin] = cost, int(coin)/(cost)

    sorted_dict = sorted(cost_value.items(), key = lambda item: -item[1][1])
    for coin, item in sorted_dict:
        while True :
            if money - int(coin)  >= 0 :
                money -= int (coin)
                answer += item[0]
            else :
                break
    return answer

    