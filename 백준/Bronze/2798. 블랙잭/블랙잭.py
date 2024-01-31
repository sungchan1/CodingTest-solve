n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = -float("inf");
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp_sum = sum([cards[i], cards[j],cards[k]]) 
            if temp_sum == m :
                result = m
                break
            elif temp_sum > result and temp_sum < m:
                result = temp_sum
            else :
                pass
            
print(result)