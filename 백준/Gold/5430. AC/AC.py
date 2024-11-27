from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    # 입력 받기
    functions = stdin.readline().strip()
    n = int(stdin.readline().strip())
    array_input = stdin.readline().strip()[1:-1]  # '['와 ']' 제거

    # 배열 초기화
    if array_input:
        q = deque(map(int, array_input.split(',')))
    else:
        q = deque()

    # 연산 처리
    forward = True
    error = False
    for func in functions:
        if func == 'R':  # 뒤집기
            forward = not forward
        elif func == 'D':  # 제거
            if not q:  # 비어있는 경우
                error = True
                break
            if forward:
                q.popleft()
            else:
                q.pop()

    # 결과 출력
    if error:
        print("error")
    else:
        if not forward:  # 뒤집힌 상태라면
            q.reverse()
        print("[" + ",".join(map(str, q)) + "]")