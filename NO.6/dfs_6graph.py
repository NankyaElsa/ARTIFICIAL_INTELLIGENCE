#N0.6a

#This program demonstrates the depth-first search algorithm for a graph using python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order.

# Step 1: Turn the graph provided into an adjacency list format or a dictionary format in python

adj_list2 = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": []
}

# Define all the variables to use
color = {}
parent = {}
trav_time = {}
output = []

# Initialize all the required variables
for node in adj_list2.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

# We start the actual algorithm by defining a function because the DFS is a recursive algorithm
time = 0
expanded_states = []  # To store the order of expanded states

def dfs(start_node):
    global time
    color[start_node] = "G"
    trav_time[start_node][0] = time
    expanded_states.append(start_node)
    time += 1

    # Traverse through every child of the current vertex
    for child in sorted(adj_list2[start_node]):  # Sort children alphabetically
        if color[child] == "W":
            parent[child] = start_node
            dfs(child)
    color[start_node] = "B"
    trav_time[start_node][1] = time
    time += 1

dfs("S")
print("Order of States Expanded:")
print(expanded_states)

# Print the path returned
goal_node = "G"
path = []
while goal_node is not None:
    path.append(goal_node)
    goal_node = parent[goal_node]
path.reverse()
print("DFS Graph Output:", path)

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(adj_list2.keys()) - set(expanded_states))
print("States Not Expanded (Alphabetical Order):")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'B', 'C', 'D', 'G']
# DFS Graph Output: ['S', 'A', 'B', 'C', 'D', 'G']
# States Not Expanded (Alphabetical Order):
# []
