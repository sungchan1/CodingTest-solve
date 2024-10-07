import sys

sys.setrecursionlimit(10 ** 6)

# 입력받기
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break


# 이진 검색 트리 구성 (반복문 사용)
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 이진 검색 트리에 노드 삽입 (반복문 사용)
def insert_iter(root, key):
    new_node = Node(key)
    current = root
    parent = None

    while current is not None:
        parent = current
        if key < current.key:
            current = current.left
        else:
            current = current.right

    if key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node


# 후위 순회 (반복문 사용)
def postorder_iter(root):
    stack = []
    last_visited = None
    current = root

    result = []

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.key)
                last_visited = stack.pop()

    # 후위 순회 결과 출력
    for value in result:
        print(value)


# 트리 생성
if preorder:
    root = Node(preorder[0])  # 첫 번째 값으로 루트 노드 생성

    for key in preorder[1:]:
        insert_iter(root, key)

    # 후위 순회 출력
    postorder_iter(root)
