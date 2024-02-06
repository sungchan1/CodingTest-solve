from sys import stdin as s
def dfs(numbers, n, m) -> None:
    if len(numbers) == m:
        print(" ".join(numbers))
        return

    for number in range(1, n+1):
        # if not str(number) in numbers:
        if not numbers or int(numbers[-1]) <= number:
            dfs(numbers + str(number), n, m)

# s = open("input.txt", "r")
n, m = map(int, s.readline().split())
dfs("", n, m)