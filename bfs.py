from collections import deque


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            return path
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited and (neighbor, path + [neighbor]) not in queue:
                queue.append((neighbor, path + [neighbor]))
    return None
