from sys import stdin as s
# s=open("input.txt","rt")

n, k = map(int, s.readline().split())
q = list(range(1, n+1))
index = k-1
result = []
while q:
    index = index % len(q)
    result.append(q.pop(index))
    index = (index + k-1)
print("<"+ ", ".join(map(str, result))+">")

