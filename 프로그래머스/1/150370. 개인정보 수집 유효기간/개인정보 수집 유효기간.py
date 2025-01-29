def convert_day(date):
    splits = list(map(int, date.split(".")))
    return splits[2] + splits[1]*28 + splits[0]*28*12


def solution(today, terms, privacies):
    answer = []
    convert_today = convert_day(today)
    terms_dict ={}
    
    
    for term in terms :
        _splits = term.split()
        terms_dict[_splits[0]] = int(_splits[1]) * 28

    for i, privacy in enumerate(privacies):
        check_day, term = privacy.split()
        end_day = convert_day(check_day) + terms_dict[term]
        if convert_today  < end_day :
            continue
        else:
            answer.append(i+1)
            
    
    return answer