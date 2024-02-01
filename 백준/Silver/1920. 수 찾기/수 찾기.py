from sys import stdin as s
# s=open("input.txt","rt")

s.readline()

sample = list(map(int, s.readline().split()))
sample.sort()
s.readline()
compare = list(map(int, s.readline().split()))

for number in compare:
    start=0
    end = len(sample) -1
    flag = False
    while start <= end:
        m = (start+end)//2
        if sample[m] == number:
            flag = True
            break
        elif sample[m] < number :
            start = m +1
        else:
            end = m -1
    if flag:
        print("1")
    else:
        print("0")




