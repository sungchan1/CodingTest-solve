from sys import stdin as s
# s=open("input.txt","rt")

def gcd(n,m):
    while m>0:
        n,m = m, n%m
    return n

a,b = map(int, s.readline().split())
gcd = gcd(a,b)
print(gcd, int(a*b/gcd))



