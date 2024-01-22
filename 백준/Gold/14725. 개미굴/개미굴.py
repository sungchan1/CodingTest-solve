class Node:
    def __init__(self, layer):
        self.bottom_layer = {}
        self.layer = layer

def dfs_print(node:Node):
    if len(node.bottom_layer.values()) == 0:
        return None
    sorted_layer = sorted(list(node.bottom_layer.items()), key=lambda x: x[0])
    for feed, bottom_node in sorted_layer:
        print("--"*bottom_node.layer + feed)
        dfs_print(bottom_node)

ants_number = int(input())
root = Node(0)

for ant in range(ants_number):
    messages = input().split()
    message_number = int(messages.pop(0)) #
    current_node = root
    for i in range(message_number):
        if messages[i] in current_node.bottom_layer.keys():
            current_node = current_node.bottom_layer[messages[i]]
        else:
            current_node.bottom_layer[messages[i]] = Node(i)
            current_node = current_node.bottom_layer[messages[i]]
            # print(messages[i], i)

dfs_print(root)


