
from collections import deque


def topological_sort(n, comparisons):
    # Initialize graph and in-degree array
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    # Build the graph
    for a, b in comparisons:
        graph[a].append(b)
        in_degree[b] += 1

    # Initialize the queue with nodes having in-degree of 0
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    result = []

    # Process nodes in topological order
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


# Read input
n, m = map(int, input().split())
comparisons = [tuple(map(int, input().split())) for _ in range(m)]

# Get the topological order
order = topological_sort(n, comparisons)

# Print the result
print(" ".join(map(str, order)))