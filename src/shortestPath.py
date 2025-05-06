import heapq

def shortest_path(graph, start_node, end_node):
    n = len(graph)
    distances = {node: float('inf') for node in range(n)}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    previous_nodes = {node: None for node in range(n)}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0:  # Only consider positive weights
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

    return reconstruct_path(previous_nodes, start_node, end_node)

def reconstruct_path(previous_nodes, start_node, end_node):
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    
    if path and path[0] == start_node:
        return path
    else:
        return []  # Return an empty list if no path is found

# Ejemplo de uso
if __name__ == "__main__":
    graph = [
        [0, 2, 6, 0, 0, 0, 0],
        [2, 0, 0, 5, 0, 0, 0],
        [6, 0, 0, 8, 0, 0, 0],
        [0, 5, 8, 0, 10, 15, 0],
        [0, 0, 0, 10, 0, 6, 2],
        [0, 0, 0, 15, 6, 0, 6],
        [0, 0, 0, 0, 2, 6, 0]
    ]
    start_node = 0
    end_node = 6
    path = shortest_path(graph, start_node, end_node)
    
    if path:
        print(f"The shortest path is through these nodes: {' -> '.join(map(str, path))}")
    else:
        print("No path found.")