
#N0.3a
#This program demonstrates the depth first tree search algorithm using python

#step1: Turn the given tree into a python dictionary format

tree2 ={
    "S":["A","B"],
    "A":["B","C"],
    "B":["C"],
    "C":["D","G"],
    "D":["G"],
    "G":[]
}
#Define all the variables to be used
trav_output = []
parent ={}
traversal_time = {}

#Initialize all the nodes to be looked at
for node in tree2.keys():
    parent[node] = None
    traversal_time[node] =[-1,-1]

print(parent)
print(traversal_time)
#Start the actual algorithm by defining a function 
time = 0
def dfs_tree(s_node):
    global time
    if node not in tree2:
        print("Node not in tree")
    traversal_time[s_node][0] = time
    trav_output.append(s_node)
    time +=1
    for child in tree2[s_node]:
        parent[child] = s_node
        dfs_tree(child)
    #happens after the for loop
    traversal_time[s_node][1] =time
    time +=1
dfs_tree("S")
print(trav_output)
print(parent)
print(traversal_time)

#print the path returned
goal_node = "G"
path = []
while goal_node is not None:
    path.append(goal_node)
    goal_node = parent[goal_node]
path.reverse()
print("==========================================")# helps me separate the path output from all other printouts
print("Depth first Search Path:", path) #Output path is ['S', 'B', 'C', 'G']

    
    