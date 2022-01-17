def solution(progresses, speeds):
    answer = []
    answer_len = len(progresses)
    while progresses :
        progresses = [progress + speed for progress,speed in zip(progresses, speeds) ]
        if progresses[0] >= 100 :
            answer.append(0)
        while progresses[0] >= 100:
            answer[-1] +=1
            progresses.pop(0)
            speeds.pop(0)
            if not progresses:
                break
    return answer