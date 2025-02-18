import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    total = max_p = flag = 0
    for _ in range(N):
        x, p = map(int, input().split())
        if total > x:
            if flag == 2 or flag and total-max_p > x:
                print('Zzz')
                return
            if total-max_p > x:
                flag = 2
                continue
            flag = 1
        total += p
        if p > max_p:
            max_p = p
    print('Kkeo-eok')

solution()