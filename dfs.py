def dfs(graph, start, goal, path=[], visited=set()):
    path = path + [start]
    if start == goal:
        return path
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None
