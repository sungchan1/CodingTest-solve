from sys import stdin
import heapq


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def range_sum(self, left, right):
        left += self.n
        right += self.n
        total = 0
        while left < right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1

            if right % 2 == 1:
                right -= 1
                total += self.tree[right]
            left //= 2
            right //= 2
        return total


n, m, k = map(int, stdin.readline().split())
data = []

for _ in range(n):
    data.append(int(stdin.readline()))

seg_tree = SegmentTree(data)



for _ in range(m + k):
    line = list(map(int, stdin.readline().split()))

    if line[0] == 1:
        index = line[1] - 1
        value = line[2]
        seg_tree.update(index, value)



    elif line[0] == 2:
        start = line[1] - 1
        end = line[2]
        print(seg_tree.range_sum(start, end))


