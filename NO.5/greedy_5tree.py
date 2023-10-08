#N0.5d
# This program demonstrates the greedy tree search algorithm using python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order
import heapq

adj_list6 = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": []
}
heuristics = {
    "S": 7,
    "A": 5,
    "B": 7,
    "C": 4,
    "D": 1,
    "G": 0
}

def greedy_tree(adj_list6, start, goal, heuristics):
    priority_queue = [(heuristics[start], start)]  # Prioritize nodes based on heuristic estimate
    heapq.heapify(priority_queue)
    parent = {}
    expanded_states = []  # To store the order of expanded states

    while priority_queue:
        current_tuple = heapq.heappop(priority_queue)
        current_node = current_tuple[1]
        expanded_states.append(current_node)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent.get(current_node)
            return expanded_states, path[::-1]

        for child in sorted(adj_list6[current_node]):  # Sort children alphabetically
            heapq.heappush(priority_queue, (heuristics[child], child))
            parent[child] = current_node

    return expanded_states, None

start = "S"
goal = "G"

expanded_states, path = greedy_tree(adj_list6, start, goal, heuristics)

if path:
    print("Order of States Expanded:")
    print(expanded_states)
    print("Greedy Tree Search Path:", path)
else:
    print("No path found (Greedy Tree Search).")

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(adj_list6.keys()) - set(expanded_states))
print("States Not Expanded (Alphabetical Order):")
print(unexpanded_states)
