# Copyright David Bai: Anyone can use this code without permission or referencing the original source
"""
W1 Kosaraju Algorithm
List Based Iterative Implementation to find sizes of strongly connected components
"""

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
num_nodes = 875715

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("SCC.txt", "r") 
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]


########################################################
# DFS on reverse graph
print('Reverse Graph')
for node in range(1, num_nodes):
    if node%1000 == 0:
        print(node)
    if visited[node] == False:
        visited[node] = True
        stack += [node]
        popped = []
        while stack:
            v = stack.pop()
            popped += [v]
            for next_node in r_gr[v]:
                if visited[next_node] == False:
                    visited[next_node] = True
                    stack += [next_node]
        order = popped + order


########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
scc_count = []

print('Original graph')
for node in order:

    if visited[node] == False:
        visited[node] = True
        stack += [node]
        count = 1
        while stack:
            v = stack.pop()
            for next_node in gr[v]:
                if visited[next_node] == False:
                    visited[next_node] = True
                    stack += [next_node]
                    count += 1
        scc_count += [count]


########################################################
# Getting the five biggest sccs
scc_count.sort(reverse=True)
print(scc_count[:5])