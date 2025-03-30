from sys import stdin
from collections import deque

input = stdin.readline


while len(data := input().split()) > 1:
    n, *heights = map(int, data)
    heights = list(heights)

    # 히스토그램 끝에 0 추가
    heights.append(0)

    stack = deque()
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            # 뒤에서 부터 가져옴
            top = stack.pop()
            height = heights[top]
            # 스택이 없으면 이전 높이도 현재 높이와 동일
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    print(max_area)