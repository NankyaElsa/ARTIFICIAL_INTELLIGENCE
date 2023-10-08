#N0.6b
#This program implements the breadth first search algorithm using python for graph, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order


from queue import Queue

# Step 1: change the graph given to you into an adjacency list format

adj_list = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": []
}

# Initialize all the necessary variables that we are going to use

queue = Queue()
visited = {}
bfs_traversal_output = []
level = {}
parent = {}

for node in adj_list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None

# Start the algorithm with the root node or start node
start_node = "S"
queue.put(start_node)
visited[start_node] = True
level[start_node] = 0

expanded_states = []  # To store the order of expanded states

while not queue.empty():
    u = queue.get()  # pop the first element of the queue
    expanded_states.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

print("Order of States Expanded:")
print(expanded_states)

# Print the path returned
Tnode = "G"
path = []
while Tnode is not None:
    path.append(Tnode)
    Tnode = parent[Tnode]
path.reverse()
print("BFS Graph Path:", path)

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(adj_list.keys()) - set(expanded_states))
print("States Not Expanded (Alphabetical Order):")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'B', 'C', 'D', 'G']
# BFS Graph Path: ['S', 'A', 'C', 'G']
# States Not Expanded (Alphabetical Order):
# []
