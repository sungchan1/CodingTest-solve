from collections import deque
from sys import stdin as s, stdout as o

def dfs(base, exponent, mod):
    if exponent == 1:
        return base % mod
    split = dfs(base, exponent//2 ,mod) % mod

    if exponent % 2 ==0:
        return (split * split) % mod
    else:
        return (((split * split) % mod ) * base ) % mod


# s = open("input.txt", "r")
a,b,c = map(int, s.readline().split())
print(dfs(a,b,c))