
#N0.4d
import heapq

adj_list5 = {
    "S":["A","B"],
    "A":["B","C"],
    "B":["C"],
    "C":["D","G"],
    "D":["G"],
    "G":[]
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

    while priority_queue:
        current_tuple = heapq.heappop(priority_queue)
        current_node = current_tuple[1]

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent.get(current_node)
            return path[::-1]

        for child in adj_list5[current_node]:
            if child not in parent:
                heapq.heappush(priority_queue, (heuristics[child], child))
                parent[child] = current_node

    return None

start = "S"
goal = "G"

path = greedy_graph(adj_list5, start, goal, heuristics)
if path:
    print("Greedy Search graph Path:", path)
else:
    print("No path found (Greedy Search).")
