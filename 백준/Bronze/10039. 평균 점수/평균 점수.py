total_score = 0
for i in range(5):
    score = int(input())
    if score >= 40 :
        total_score += score
    else :
        total_score += 40

print(int(total_score/5))