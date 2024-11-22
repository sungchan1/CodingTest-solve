from sys import stdin


class MaxSegTree:

    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [float("-inf")] * self.n * 2
        self.build()

    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = self.data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, start, end):
        left = start + self.n
        right = end + self.n

        result = float("-inf")

        while left <= right:

            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1

            if right % 2 == 0:
                result = max(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result


class MinSegTree:

    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.tree = [float("inf")] * (self.n * 2)
        self.build()

    def build(self):

        for i in range(self.n):
            self.tree[self.n + i] = self.data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, start, end):
        left = start + self.n
        right = end + self.n

        result = float("inf")

        while left <= right:

            if left % 2 == 1:
                result = min(result, self.tree[left])
                left += 1

            if right % 2 == 0:
                result = min(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result


n, m = map(int, stdin.readline().split())

numbers = []

for _ in range(n):
    numbers.append(int(stdin.readline()))

max_tree = MaxSegTree(numbers)
min_tree = MinSegTree(numbers)

for _ in range(m):
    start, end = map(int, stdin.readline().split())

    range_min, range_max = min_tree.query(start - 1, end - 1), max_tree.query(start - 1, end - 1)
    print(range_min, range_max)
