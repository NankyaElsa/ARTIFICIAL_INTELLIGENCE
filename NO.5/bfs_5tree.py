# N0.5b
# This program implements the breadth-first tree search algorithm in python, prints out
#the order of states expanded, the path returned and the states that are not expanded assuming
#ties are broken in alphabetical order

from queue import Queue

# Step 1: Change the given tree into a Python dictionary

tree = {
    "S": ["A", "B"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D", "G"],
    "D": ["G"],
    "G": []
}

# Initialize all the variables that are going to be used

queue = Queue()
output = []
level = {}
parent = {}

for node in tree.keys():
    level[node] = -1
    parent[node] = None

# Start the algorithm by adding the root node to the queue

s_node = "S"
queue.put(s_node)
level[s_node] = 0

while not queue.empty():
    i = queue.get()  # Pop the first node in the queue
    output.append(i)

    children = sorted(tree[i])  # Sort children alphabetically
    for j in children:
        parent[j] = i
        level[j] = level[i] + 1
        queue.put(j)

print("Order of States Expanded:")
print(output)
print("Path Returned by Algorithm:")
w_node = "G"
path = []
while w_node is not None:
    path.append(w_node)
    w_node = parent[w_node]
path.reverse()
print("Path:", path)

# States that are not expanded (assuming ties are broken in alphabetical order)
unexpanded_states = sorted(set(tree.keys()) - set(output))
print("States Not Expanded (Alphabetical Order):")
print(unexpanded_states)

#output
# Order of States Expanded:
# ['S', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'G', 'D', 'G', 'D', 'G', 'G', 'G', 'G']
# Path Returned by Algorithm:
# Path: ['S', 'A', 'B', 'C', 'D', 'G']
# States Not Expanded (Alphabetical Order):
# []

