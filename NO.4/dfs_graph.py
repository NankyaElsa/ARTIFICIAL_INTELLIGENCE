
#N0.4a
#This program demonstrates the depth first search algorithm using python

#step1: Turn the graph provided into an adjacency list format or a dictionary format in python

adj_list2 = {
    "S":["A","B"],
    "A":["B","C"],
    "B":["C"],
    "C":["D","G"],
    "D":["G"],
    "G":[]
}

#Define all the variables to use
color = {}
parent = {}
trav_time = {}
output = []

#Initialise all the required variables
for node in adj_list2.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]
print(color)
print(parent) 
print(trav_time)  

#We start the actual algorithm by defining a function because the dfs is a recursive algorithm
time = 0
def dfs(start_node):
    global time
    color[start_node] = "G"
    trav_time[start_node][0] = time
    output.append(start_node)
    time +=1

    #Traverse through every child of the current vertex
    for child in adj_list2[start_node]:
        if color[child] =="W":
            parent[child] = start_node
            dfs(child)
    color[start_node] = "B"
    trav_time[start_node][1] = time
    time +=1
dfs("S")
print(output) # ['S', 'A', 'C', 'D', 'G', 'B'] The dfs algorithm removes unnecessary edges from the graph
print(trav_time)
print(parent)

#print the path returned
goal_node = "G"
path = []
while goal_node is not None:
    path.append(goal_node)
    goal_node = parent[goal_node]
path.reverse()
print("DFS graph output", path)
