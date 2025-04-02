from sys import stdin


class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (self.n * 4)
        self.build(data, 0, self.n - 1, 1)

    def build(self, data, left, right, node):
        if left == right:
            self.tree[node] = (data[left], left)  # 값, 인덱스
            return

        mid = (left + right) // 2
        self.build(data, left, mid, node * 2)
        self.build(data, mid + 1, right, node * 2 + 1)

        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])  # (값, 인덱스)

    def query(self, ql, qr, left=0, right=None, node=1):
        if right is None:
            right = self.n - 1

        if qr < left or ql > right:
            return (float('inf'), float('inf'))

        if ql <= left and right <= qr:
            return self.tree[node]

        mid = (left + right) // 2
        left_min = self.query(ql, qr, left, mid, node * 2)
        right_min = self.query(ql, qr, mid + 1, right, node * 2 + 1)

        return min(left_min, right_min)

    def update(self, index, value, left=0, right=None, node=1):
        if right is None:
            right = self.n - 1

        if index < left or index > right:
            return

        if left == right:
            self.tree[node] = (value, index)
            return

        mid = (left + right) // 2
        self.update(index, value, left, mid, node * 2)
        self.update(index, value, mid + 1, right, node * 2 + 1)

        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])



input = stdin.readline


n = int(input())
data = list(map(int, input().split()))
seg_tree = SegmentTree(data)

query_number = int(input())
for _ in range(query_number):
    command, i, j = map(int, input().split())

    if command == 1:
        seg_tree.update(i - 1, j)  # 1-based → 0-based
    elif command == 2:
        _, idx = seg_tree.query(i - 1, j - 1)  # 1-based → 0-based
        print(idx + 1)  # 다시 1-based로 출력


