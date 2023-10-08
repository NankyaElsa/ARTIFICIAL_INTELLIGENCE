
#NO.3e
#This program demonstrates the A* tree search algorithm using python
import heapq

# Define the adjacency list and heuristics 
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

def astar_tree(adj_list4, start, goal, heuristics):
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    parent = {}

    while priority_queue:
        current_tuple = heapq.heappop(priority_queue)
        current_cost = current_tuple[0]
        current_node = current_tuple[1]

        if current_node == goal:
            # Reconstruct the path from the goal to the start
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent.get(current_node)  # Use parent pointers
            return path[::-1]

        for child, cost in adj_list4[current_node].items():
            # Calculate the current cost for the child
            current_cost = current_tuple[0] + cost + heuristics[child]
            # Add the child to the priority queue with the new current cost
            heapq.heappush(priority_queue, (current_cost, child))
            # Set the parent of the child
            parent[child] = current_node

    return None

start = "S"
goal = "G"

path = astar_tree(adj_list4, start, goal, heuristics)
if path:
    print("A Star tree search:", path) #A Star tree search: ['S', 'A', 'B', 'C', 'G']
else:
    print("No path found for A star tree search")
