#N0.5a

# This program demonstrates the depth-first tree search algorithm using python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order

# Step 1: Turn the given tree into a python dictionary format

tree2 = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": []
}

# Define all the variables to be used
trav_output = []
parent = {}
traversal_time = {}

# Initialize all the nodes to be looked at
for node in tree2.keys():
    parent[node] = None
    traversal_time[node] = [-1, -1]

# Start the actual algorithm by defining a function
time = 0


def dfs_tree(s_node):
    global time
    if s_node not in tree2:
        print("Node not in tree")
    traversal_time[s_node][0] = time
    trav_output.append(s_node)
    time += 1
    children = sorted(tree2[s_node])
    for child in children:
        parent[child] = s_node
        dfs_tree(child)
    # Happens after the for loop
    traversal_time[s_node][1] = time
    time += 1


dfs_tree("S")
print("Order of States Expanded:")
print(trav_output)
print("Path Returned by Algorithm:")
goal_node = "G"
path = []
while goal_node is not None:
    path.append(goal_node)
    goal_node = parent[goal_node]
path.reverse()
print("Path:", path)

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(tree2.keys()) - set(trav_output))
print("States Not Expanded:")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'B', 'C', 'D', 'G', 'G', 'C', 'D', 'G', 'G', 'B', 'C', 'D', 'G', 'G']
# Path Returned by Algorithm:
# Path: ['S', 'B', 'C', 'G']
# States Not Expanded:
# []
