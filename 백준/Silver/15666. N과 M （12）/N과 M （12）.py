from sys import stdin as s

def dfs(input_numbers, numbers, n, m) -> None:
    if len(numbers) == m:
        print(" ".join(map(str, numbers)))
        return
    prints = set()
    for index, number in enumerate(input_numbers):
        if number in prints:
            pass
        elif not numbers or numbers[-1] <= number:
            prints.add(number)
            dfs(input_numbers[:],  numbers[:] + [number], n, m)

# s = open("input.txt", "r")
n, m = map(int, s.readline().split())
input_numbers = sorted(list(map(int, s.readline().split())))
dfs(input_numbers,[], n, m)