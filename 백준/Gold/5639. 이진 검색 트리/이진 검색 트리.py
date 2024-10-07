import sys

sys.setrecursionlimit(10 ** 6)


stack = []
while True:
    try:
        stack.append(int(input()))
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


    for value in result:
        print(value)




if stack:
    root = Node(stack[0])

    for key in stack[1:]:
        insert_iter(root, key)


    postorder_iter(root)
