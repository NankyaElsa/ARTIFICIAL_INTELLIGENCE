
#N0.4b
#This program implements the breadth first search algorithm using python for graph

from queue import Queue

#Step 1: change the graph given to you into an adjacency list format

adj_list = {
    "S":["A","B"],
    "A":["B","C"],
    "B":["C"],
    "C":["D","G"],
    "D":["G"],
    "G":[]
}
#Initialise all the necessary variables that we are going to use

queue = Queue()
visited = {}
bfs_traversal_output = []
level = {}
parent = {}

for node in adj_list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None

# print(visited)
# print(level)
# print(parent)

#Start the algorithm with the root node or start node
start_node = "S"
queue.put(start_node)
visited[start_node] = True
level[start_node] = 0

while  not queue.empty():
    u = queue.get() #pop the first element of the queque
    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] +1
            queue.put(v)

print(bfs_traversal_output)
print(visited)
print(parent)

#print the path returned
Tnode = "G"
path = []
while Tnode is not None:
    path.append(Tnode)
    Tnode = parent[Tnode]
path.reverse()
print("BFS graph path ",path)
