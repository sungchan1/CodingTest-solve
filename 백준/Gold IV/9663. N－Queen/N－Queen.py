import time
from sys import stdin as s

# s = open("input.txt", r)

def n_queens_optimized(n):
    def solve(row, cols, diags, anti_diags):
        if row == n:
            return 1
        solutions = 0
        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col
            if col in cols or curr_diag in diags or curr_anti_diag in anti_diags:
                continue
            cols.add(col)
            diags.add(curr_diag)
            anti_diags.add(curr_anti_diag)
            solutions += solve(row + 1, cols, diags, anti_diags)
            cols.remove(col)
            diags.remove(curr_diag)
            anti_diags.remove(curr_anti_diag)
        return solutions

    return solve(0, set(), set(), set())

n = int(s.readline())
print(n_queens_optimized(n))