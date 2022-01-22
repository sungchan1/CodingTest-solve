def solution(answers):
    
    first_person = [1,2,3,4,5]
    second_person = [2,1,2,3,2,4,2,5]
    third_person = [3,3,1,1,2,2,4,4,5,5]
    
    score = []
    score.append([0,1])
    score.append([0,2])
    score.append([0,3])

    for index , answer in enumerate(answers) :
        if first_person[index%5] == answer :
            score [0][0] +=1
        if second_person[index%8] == answer :
            score [1][0] +=1
        if third_person[index%10] == answer :
            score [2][0] +=1
    
    score_sorted= sorted(score, key = lambda x : ( -x[0], x[1] ))
    
    answer = []
    answer.append(score_sorted[0][1])
    print(score_sorted)
    if score_sorted[0][0] == score_sorted[1][0]:
        answer.append(score_sorted[1][1])
        if score_sorted[1][0] == score_sorted[2][0]:
            answer.append(score_sorted[2][1])

    return answer