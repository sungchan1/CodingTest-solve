test_number = int(input())


for i in range(test_number):
    yonsei_total = 0
    korea_total = 0
    for j in range(9):
        yonsei_score, korea_score = map(int, input().split())
        yonsei_total += yonsei_score
        korea_total += korea_score

    message = ""
    if yonsei_total == korea_total:
        message = "Draw"
    elif yonsei_total > korea_total :
        message = "Yonsei"
    else :
        message = "Korea"
    print(message)



