from collections import deque

def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    start_indexes = [start_index for start_index in range(len(tickets)) if tickets[start_index][0] == "ICN"]
    answer = 0
    for start_index in start_indexes:
        if answer:
            continue
        dq = deque([[start_index]])
        while dq:
            cur_idxs = dq.popleft()
            if len(cur_idxs) == len(tickets):
                answer = [tickets[x][0] for x in cur_idxs] + [tickets[cur_idxs[-1]][1]]
                break
            cur_idx = cur_idxs[-1]
            for idx in range(len(tickets)):
                if idx not in cur_idxs and tickets[cur_idx][1] == tickets[idx][0]:
                    dq.append(cur_idxs+[idx])
    return answer