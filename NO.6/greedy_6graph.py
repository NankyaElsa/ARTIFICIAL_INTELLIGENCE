#N0.6d
# This program demonstrates the greedy graph search algorithm using python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order

import heapq

adj_list5 = {
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

def greedy_graph(adj_list5, start, goal, heuristics):
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

        for child in sorted(adj_list5[current_node]):  # Sort children alphabetically
            if child not in parent:
                heapq.heappush(priority_queue, (heuristics[child], child))
                parent[child] = current_node

    return expanded_states, None

start = "S"
goal = "G"

expanded_states, path = greedy_graph(adj_list5, start, goal, heuristics)

if path:
    print("Order of States Expanded:")
    print(expanded_states)
    print("Greedy Search Graph Path:", path)
else:
    print("No path found (Greedy Search).")

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(adj_list5.keys()) - set(expanded_states))
print("States Not Expanded (Alphabetical Order):")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'C', 'G']
# Greedy Search Graph Path: ['S', 'A', 'C', 'G']
# States Not Expanded (Alphabetical Order):     
# ['B', 'D']
