#N0.5e
#This program demonstrates the A* tree search algorithm using python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order
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
    expanded_states = []  # To store the order of expanded states

    while priority_queue:
        current_tuple = heapq.heappop(priority_queue)
        current_cost = current_tuple[0]
        current_node = current_tuple[1]
        expanded_states.append(current_node)

        if current_node == goal:
            # Reconstruct the path from the goal to the start
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent.get(current_node)  # Use parent pointers
            return expanded_states, path[::-1]

        for child, cost in adj_list4[current_node].items():
            # Calculate the current cost for the child
            current_cost = current_tuple[0] + cost + heuristics[child]
            # Add the child to the priority queue with the new current cost
            heapq.heappush(priority_queue, (current_cost, child))
            # Set the parent of the child
            parent[child] = current_node

    return expanded_states, None

start = "S"
goal = "G"

expanded_states, path = astar_tree(adj_list4, start, goal, heuristics)

if path:
    print("Order of States Expanded:")
    print(expanded_states)
    print("A Star Tree Search Path:", path)
else:
    print("No path found for A star tree search")

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(adj_list4.keys()) - set(expanded_states))
print("States Not Expanded:")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'B', 'C', 'C', 'B', 'G']
# A Star Tree Search Path: ['S', 'A', 'B', 'C', 'G']
# States Not Expanded:
# ['D']
