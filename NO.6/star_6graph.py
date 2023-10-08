#N0.6e
#This program demonstrates the A* graph search algorithm using python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order
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
    expanded_states = []  # To store the order of expanded states

    while priority_queue:
        current_tuple = heapq.heappop(priority_queue)
        current_cost = current_tuple[0]
        current_node = current_tuple[1]
        expanded_states.append(current_node)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return expanded_states, path[::-1]

        for child, cost in adj_list4[current_node].items():
            actual_cost = edge[current_node] + cost

            if actual_cost < edge[child]:
                edge[child] = actual_cost
                current_cost = edge[current_node] + cost + heuristics[child]
                heapq.heappush(priority_queue, (current_cost, child))
                parent[child] = current_node

    return expanded_states, None

start = "S"
goal = "G"

expanded_states, path = star_graph(adj_list4, start, goal, heuristics)

if path:
    print("Order of States Expanded:")
    print(expanded_states)
    print("Shortest Path Star graph:", path)
else:
    print("No path found.")

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(adj_list4.keys()) - set(expanded_states))
print("States Not Expanded (Alphabetical Order):")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'B', 'C', 'G']
# Shortest Path Star graph: ['S', 'B', 'C', 'G']
# States Not Expanded (Alphabetical Order):
# ['D']