input()
numbers = list(map(int, input().split()))
max_num = max(numbers)

print(sum(numbers)/len(numbers)/max_num*100)
