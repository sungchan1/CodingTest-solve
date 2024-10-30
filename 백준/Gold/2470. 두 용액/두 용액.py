import heapq
from sys import stdin


n = int(stdin.readline())

liquids = list(map(int, stdin.readline().split()))
liquids.sort()
q = []



left = 0
right = n -1


while left < right:
    ph = liquids[right] + liquids[left]
    # print(left, right, ph)

    heapq.heappush(q, (abs(ph), left, right))


    if ph == 0:
        break

    elif ph > 0:
        right -=1
    else:
        left += 1


# print(q)

print(liquids[q[0][1]], liquids[q[0][2]])