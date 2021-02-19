'''
Implementation of Floyd Warshall Algorithm
'''
# TODO: Johnson's Algorithm

import sys

filename = sys.argv[1]

lines = open(filename, 'r').readlines()
num_v, num_e = lines.pop(0).strip().split(' ')
num_v = int(num_v)

# Using nested dict to store the graph
print("Initializing graph")
graph = {}
for line in lines:
    start, end, weight = line.strip().split(' ')
    if int(start) not in graph:
        graph[int(start)] = {}
    graph[int(start)][int(end)] = int(weight)

# Initializing 2 nested lists
old = [[float("inf") for i in range(num_v)] for j in range(num_v)]
new = [[0 for i in range(num_v)] for j in range(num_v)]

# Initializing k = 0
# Assume all vertices have edge from them
print("Initializing k = 0")
for i in range(num_v):
    for j in range(num_v):
        if i == j:
            old[i][j] = 0
        if j+1 in graph[i+1]:
            old[i][j] = graph[i+1][j+1]

print("Obtaining shortest path")
for k in range(num_v):
    if k%100 == 0:
        print(k)
    for i in range(num_v):
        for j in range(num_v):
            new[i][j] = min(old[i][j], old[i][k]+old[k][j])
    old = new

if any(new[i][i]<0 for i in range(num_v)):
    print("Negative cycle detected")
print("Shortest path :", min([min(new[i]) for i in range(num_v)]))