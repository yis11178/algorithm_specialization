'''
Implementation of Prim's algorithm
to solve Minimum Spanning Tree problem
'''

import sys
import heapq

filename = sys.argv[1]
graph = []


lines = open(filename, 'r').readlines()
num_nodes, num_edges = lines.pop(0).strip().split(' ')
num_nodes = int(num_nodes)
for line in lines:
    line = line.strip().split(' ')
    line = [int(i) for i in line]
    graph += [line]

'''
1. Start with arbitrary node
2. Add new node to MST
3. Update frontier of MST
4. Select edge with cheapest cost
5. Destination of that edge is newly explored node
6. Repeat step 2~5

Note: 
Not necessary to track all the explored node
Whats Important is change in frontier brought by new node
Theoretical time complexity O(mlogn)
'''
def prim(graph):
    # Arbitrary starting point, say it 1. 
    u = 1
    # the cost to span node 1 to node 1 is ignored
    # Inf represents node with no connection from MST
    heap_node = [[float('inf'), i] for i in range(2, num_nodes+1)]
    total_cost = 0
    # Note that update of the key in heap is done by search
    # which running time is O(n)
    # It should be updated with decrease-key operation
    # which running time is O(logn)
    while heap_node:
        for edge in graph:
            # Find all adjacency node of u
            # Update the cost to adjacency node if the cost is lower than 
            # previous value in heap
            if u in edge[:-1]:
                pos = edge[:-1].index(u)
                heap_node = [[edge[-1], edge[1-pos]] if (edge[1-pos]==x[1] and edge[-1]<x[0]) 
                            else x for x in heap_node]
                heapq.heapify(heap_node)
        # Remove explored edges
        graph = [edge for edge in graph if u not in edge[:-1]]
        # Remove from heap (which is unexplored)
        cost, v = heapq.heappop(heap_node)
        total_cost += cost
        # Equivalently add v to MST 
        u = v
    return total_cost

print('Total cost for MST is: ', prim(graph))