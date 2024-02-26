import heapq


def dijkstra(graph, start, goal):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == goal:
            break

        for neighbor, attrs in graph[current_node].items():
            distance = current_distance + attrs["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current_node = goal
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return path
