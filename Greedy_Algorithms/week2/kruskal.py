from networkx.utils import UnionFind
import sys

filename, k = sys.argv[1:3]
k = int(k)
graph = []

lines = open(filename, 'r').readlines()
num_nodes = int(lines.pop(0).strip())
# Each node's leader is initialized to itself
uf = UnionFind([i for i in range(1, num_nodes+1)])

for line in lines:
    line = line.strip().split(' ')
    line = [int(i) for i in line]
    graph += [line]

# Sort the edges in increasing order of cost
graph.sort(key=lambda x:x[-1])

for edge in graph:
    # Iterate until the desired number of clusters (k) is obtained
    # Initial number of clusters = number of nodes
    if num_nodes == k:
        break
    start, end, cost = edge
    # If an edge with ends in different group
    # fuse the group
    if uf[start] != uf[end]:
        uf.union(start, end)
        num_nodes -= 1

# Iterate throught the edges (sorted)
# to find the edge with ends in different cluster 
# and minimum cost
for edge in graph:
    start, end, cost = edge
    if uf[start] != uf[end]:
        break
print('The minimum spacing for the clustering is :', cost)