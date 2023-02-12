
import sys
def solution(numbers):
    def search(left, right, index, total):
        if len(numbers) == index:
            return total
        if left == right:
            return float('inf')
        number = int(numbers[index])
        left_total = search(number, right, index + 1, total) + weights[left][number]
        right_total = search(left, number, index + 1, total) + weights[right][number]
        return min(left_total, right_total)

    
    sys.setrecursionlimit(300_000)
    weights = ((1, 7, 6, 7, 5, 4, 5, 3, 2, 3),
               (7, 1, 2, 4, 2, 3, 5, 4, 5, 6),
               (6, 2, 1, 2, 3, 2, 3, 5, 4, 5),
               (7, 4, 2, 1, 5, 3, 2, 6, 5, 4),
               (5, 2, 3, 5, 1, 2, 4, 2, 3, 5),
               (4, 3, 2, 3, 2, 1, 2, 3, 2, 3),
               (5, 5, 3, 2, 4, 2, 1, 5, 3, 2),
               (3, 4, 5, 6, 2, 3, 5, 1, 2, 4),
               (2, 5, 4, 5, 3, 2, 3, 2, 1, 2),
               (3, 6, 5, 4, 5, 3, 2, 4, 2, 1))
    return search(4, 6, 0, 0)