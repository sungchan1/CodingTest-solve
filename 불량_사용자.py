from copy import deepcopy

def solution(user_id, banned_id):
    candidates = []

    for ban_id in banned_id:
        temp = []
        for user_full_id in user_id:
            if len(user_full_id) == len(ban_id):
                for i in range(len(user_full_id)):
                    if ban_id[i] == '*' or ban_id[i] == user_full_id[i]:
                        continue
                    else:
                        break
                else:
                    temp.append(user_full_id)
        if temp:
            candidates.append(temp)
        

    results = set()
    dfs(candidates, user_id, [], results)
    
    return len(results)

def dfs(candidates, users, result, results):
    
    if not candidates:
        results.add(tuple(sorted(result)))
        return 
        
    new_candidates = deepcopy(candidates)
    curr = new_candidates.pop()
    for user in curr:
        if user in users:

            new_result = deepcopy(result)
            new_result.append(user)
            new_users = deepcopy(users)
            new_users.remove(user)
            
            dfs(new_candidates, new_users, new_result, results)