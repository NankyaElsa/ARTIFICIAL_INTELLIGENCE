#N0.3b
#This program implements the breadth first tree search algorithm in python

from queue import Queue

#Step 1: Change the tree given to you into a python dictionary

tree = {
    "S":["A","B"],
    "A":["B","C"],
    "B":["C"],
    "C":["D","G"],
    "D":["G"],
    "G":[]
}

#Initialize all the variables that are going to be used

queue = Queue()
output = []
level = {}
parent = {}

for node in tree.keys():
    level[node] = -1
    parent[node] = None
print(level)
print(parent)

#Start the algorithm by adding the root node to the queue

s_node = "S"
queue.put(s_node)
level[s_node] = 0

while not queue.empty():
    i = queue.get() #pop the first node in the queue
    output.append(i)

    for j in tree[i]:
        parent[j] = i
        level[j] = level[i] + 1
        queue.put(j)
print(output)
print(parent)
print(level)

#print the path returned
w_node = "G"
path = []
while w_node is not None:
    path.append(w_node)
    w_node = parent[w_node]
path.reverse()
print("==========================================")# helps me separate the path output from all other printouts 
print("Breadth first Search Path:", path) #Out put path is ["S", "A", "B", "C", "D", "G"]