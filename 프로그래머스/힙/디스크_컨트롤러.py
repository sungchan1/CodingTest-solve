import heapq  
def solution(jobs):
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    number = len(jobs)
    time = 0
    process_time = 0
    ready_queue = list()
    is_process = False
    answer = 0
    while jobs or ready_queue :
        while jobs and time == jobs[0][0]:
            ready_queue.append(jobs.pop(0)[1])
        ready_queue.sort()
        if process_time <= 0 :
            is_process = False
        else :
            is_process = True
        if  is_process :
            pass
        elif ready_queue  :
            process_time = ready_queue.pop(0)
            answer += process_time
        answer += len(ready_queue)
        time += 1
        process_time -=1 
    return int(answer/number)

