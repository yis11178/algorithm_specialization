from networkx.utils import UnionFind
from itertools import combinations
import sys

filename = sys.argv[1]
graph = {}

lines = open(filename, 'r').readlines()
num_nodes, num_bits = lines.pop(0).strip().split()
num_bits = int(num_bits)

# bit mask for Hamming distance = 1
# i.e. 0000010000 
# Masking it with node will give node that is 1 hamming distance away
check_list = [1 << i for i in range(num_bits)]
# Add bit mask for Hamming distance = 2
check_list += [(1<<i[0])+(1<<i[1]) for i in combinations(list(range(num_bits)), 2)]

for line in lines:
    # Convert bit string to integer numebr
    line = int(''.join(line.split()),2)
    # All nodes are intialized to be unvisited
    graph[line] = None

# Keep track of clustering
cluster = UnionFind(graph)
# Number of clusters initially
# This is not the same as number of nodes
# due to duplicate of nodes
k = len(graph)
for node in graph:
    for masked in [node^mask for mask in check_list]:
        # Use graph instead of list to reduce running time for search
        # Union operation only when masked and node in different group
        if masked in graph:
            if cluster[node] != cluster[masked]:
                cluster.union(masked,node)
                k -= 1

print('Maximum number of cluster with spacing at least 3 :', k)