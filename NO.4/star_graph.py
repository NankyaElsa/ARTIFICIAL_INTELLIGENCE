#N0.4e

import heapq

adj_list4 = {
    "S": {"A": 3, "B": 1},
    "A": {"B": 2, "C": 2},
    "B": {"C": 3},
    "C": {"D": 4, "G": 4},
    "D": {"G": 1},
    "G": {}
}
heuristics = {
    "S": 7,
    "A": 5, 
    "B": 7, 
    "C": 4, 
    "D": 1, 
    "G": 0
}

def star_graph(adj_list4, start, goal, heuristics):
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    edge = {}
    parent = {}

    for node in adj_list4:
        edge[node] = float('inf')  # Initialize all edge costs to infinity
        parent[node] = None

    edge[start] = 0  # Set the cost of the start node to 0

    while priority_queue:
        current_tuple = heapq.heappop(priority_queue)
        current_cost = current_tuple[0]
        current_node = current_tuple[1]

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]

        for child, cost in adj_list4[current_node].items():
            actual_cost = edge[current_node] + cost

            if actual_cost < edge[child]:
                edge[child] = actual_cost
                current_cost = edge[current_node] + cost + heuristics[child]
                heapq.heappush(priority_queue, (current_cost, child))
                parent[child] = current_node

    return None

start = "S"
goal = "G"

path = star_graph(adj_list4, start, goal, heuristics)
if path:
    print("Shortest Path Star grapg:", path)
else:
    print("No path found.")
