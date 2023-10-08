#NO.3 C
#This program demonstrates the Uniform cost search algorithm using python
import heapq

# Step 1: Turn the given tree into a python dictionary format

adj_list3 = {
    "S": {"A": 3, "B": 1},
    "A": {"B": 2, "C": 2},
    "B": {"C": 3},
    "C": {"D": 4, "G": 4},
    "D": {"G": 1},
    "G": {}
}

def ucs_tree_search(graph, start, goal):
    # Our priority queue is going to have cost node pairs in the form of a tuple
    priority_queue = [(0, start)]
    parent = {}

    while priority_queue:  # while queue is not empty
        current_tuple = heapq.heappop(priority_queue)  # pop and return the first tuple in our queue
        current_cost = current_tuple[0]
        current_node = current_tuple[1]

        if current_node == goal:
            # Print the path taken
            path = []
            while current_node in parent:
                path.insert(0, current_node)
                current_node = parent[current_node]
            path.insert(0, start)
            print("Path Taken:", "->".join(path))
            return path

        for child, cost in adj_list3.get(current_node, {}).items():
            parent[child] = current_node  # Set the parent of the child
            heapq.heappush(priority_queue, (current_cost + cost, child))
    return None

start_node = 'S'
goal_node = 'G'

result = ucs_tree_search(adj_list3, start_node, goal_node)

if result:
    print("Shortest Path FOR UCS:", result) #Path Taken: S->A->B->C->D->G
                                        #Shortest Path FOR UCS: ['S', 'A', 'B', 'C', 'D', 'G']
else:
    print("No path found.")

