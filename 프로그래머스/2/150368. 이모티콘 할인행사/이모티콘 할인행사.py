def dfs(discount_consumer, costs, emoticons, emoticon_discounts, i):
    discounts = [10,20,30,40]
    
    result_user = 0
    result_sale = 0
    

    # 정산
    if len(emoticons) == i:
        perchaces = [0 for _ in costs]
        for price, emoticon_discount in zip(emoticons, emoticon_discounts):
            _price = price * (1 - emoticon_discount * 0.01)
            for consumer in discount_consumer[emoticon_discount]:
                perchaces[consumer] += _price
                
        for cost, perchace in zip(costs, perchaces):
            if cost <= perchace :
                result_user += 1
            else:
                result_sale += perchace
        return result_user, result_sale
            
    
    
    # 할인율 돌려가며
    for discount in discounts:
        plus_users, sale= dfs(discount_consumer, costs, emoticons, emoticon_discounts+[discount], i+1)
        if result_user < plus_users:
            result_user = plus_users
            result_sale = sale
        elif result_user == plus_users:
            result_sale = max(result_sale, sale)
    
    return result_user, result_sale

def solution(users, emoticons):

    discount_to_buy = { discount:[] for discount in range(10,50,10)}
    costs = [ user[1] for user in users]
    
    for i, user in enumerate(users):
        discount, cost = user
        if discount <= 10:
            discount_to_buy[10].append(i)
        if discount <= 20:
            discount_to_buy[20].append(i)
        if discount <= 30:
            discount_to_buy[30].append(i)
        if discount <= 40:
            discount_to_buy[40].append(i)
            
    answer = dfs(discount_to_buy, costs, emoticons, [], 0)
        
    return answer