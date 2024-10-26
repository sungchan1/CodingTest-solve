import bisect


n = int(input())

numbers = list(map(int, input().split()))

sub = []


for number in numbers:

    pos = bisect.bisect_left(sub, number)

    if pos < len(sub):
        sub[pos] = number
    else:
        sub.append(number)


print(len(sub))