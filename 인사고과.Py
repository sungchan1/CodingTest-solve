def solution(scores):
    answer = 0
    if len(scores) == 1:
        return 1
    wanho_score = scores[0][1] + scores[0][0]
    # sorted_scores = sorted(scores, key=lambda x : (-x[0], -x[1]))
    sorted_scores = sorted(scores, key=lambda x : (-x[0], x[1]))
    # before_attitude_score = sorted_scores[0][0]
    max_reputation_score = sorted_scores[0][1]
    incentive_list = []     
    for attitude_score, reputation_score in sorted_scores:
        if reputation_score >= max_reputation_score :
            incentive_list.append(attitude_score +reputation_score)
            max_reputation_score =reputation_score
        # elif before_attitude_score == attitude_score :
        #     incentive_list.append(attitude_score +reputation_score)
        else :
            if attitude_score == scores[0][0]  and reputation_score == scores[0][1]:
                return -1 
    incentive_list.sort(reverse=True)
    answer= incentive_list.index(wanho_score)+1
    return answer