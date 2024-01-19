test_case = int(input())
for i in range(test_case):
    n, m = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, n, m, n+m))