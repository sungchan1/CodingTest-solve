from sys import stdin as s
# s = open("input.txt", "r")
def pre_fix(nodes, node) -> str:
    result = node
    left_leaf = nodes[node][0]
    right_leaf = nodes[node][1]
    if left_leaf != '.':
        result += pre_fix(nodes, left_leaf)
    if right_leaf != '.':
        result += pre_fix(nodes, right_leaf)
    return result

def post_fix(nodes, node) -> str:
    result = ""
    left_leaf = nodes[node][0]
    right_leaf = nodes[node][1]
    if left_leaf != '.':
        result += post_fix(nodes, left_leaf)
    if right_leaf != '.':
        result += post_fix(nodes, right_leaf)
    result += node
    return result


def in_fix(nodes, node) -> str:
    result = ""
    left_leaf = nodes[node][0]
    right_leaf = nodes[node][1]
    if left_leaf != '.':
        result += in_fix(nodes, left_leaf)
    result += node
    if right_leaf != '.':
        result += in_fix(nodes, right_leaf)
    return result


node_number = int(s.readline())
nodes = {}
for node in range(node_number):
    node, leaf_1, leaf_2 = s.readline().split()
    nodes[node] = [leaf_1, leaf_2]

start = list(nodes.keys())[0]
print(pre_fix(nodes, start))
print(in_fix(nodes, start))
print(post_fix(nodes, start))