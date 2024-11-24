from sys import stdin

modular = 1_000_000_007

class SegTree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
        self.tree = [1] * self.n * 2
        self.build()

    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = self.data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = (self.tree[2 * i] * self.tree[2 * i + 1]) % modular

    def query(self, start, end):
        left = start + self.n
        right = end + self.n
        result = 1

        while left <= right:
            if left % 2 == 1:
                result = result * self.tree[left] % modular
                left += 1
            if right % 2 == 0:
                result = result * self.tree[right] % modular
                right -= 1
            left //= 2
            right //= 2

        return result

    def update(self, index, number):
        index += self.n
        self.tree[index] = number

        while index > 1:
            index //= 2
            self.tree[index] = (self.tree[2 * index] * self.tree[2 * index + 1]) % modular


# 입력 처리
n, m, k = map(int, stdin.readline().strip().split())
numbers = [int(stdin.readline().strip()) for _ in range(n)]

# 세그먼트 트리 생성
seg_tree = SegTree(numbers)

# 명령 처리
for _ in range(m + k):
    command, x, y = map(int, stdin.readline().strip().split())
    if command == 1:
        seg_tree.update(x - 1, y)  # 업데이트
    elif command == 2:
        print(seg_tree.query(x - 1, y - 1))  # 쿼리
