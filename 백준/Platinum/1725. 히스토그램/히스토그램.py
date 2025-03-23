from sys import stdin
from collections import deque

n = int(stdin.readline())
heights = []

for _ in range(n):
    h = int(stdin.readline())
    heights.append(h)

# 히스토그램 끝에 0 추가 (모든 높이 처리 위해)
heights.append(0)

stack = deque()
max_area = 0

for i, h in enumerate(heights):
    while stack and heights[stack[-1]] > h:
        top = stack.pop()
        height = heights[top]
        # 스택이 비었으면 현재 인덱스가 너비
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, height * width)
    stack.append(i)

print(max_area)