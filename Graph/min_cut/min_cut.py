import numpy as np
import sys
import random

def merge_node(v, e):
    # v is the list of 'super node'
    # each element of v contains node that has been merged
    l = len(v)
    for i in range(l-2):
        # Note: cannot choose two nodes at random since they may not connet
        # Choose one node at random at an adjacent one at random
        [pos1]= random.sample(range(len(v)), 1)
        [second_node] = random.sample(e[pos1], 1)
        [super_node] = [x for x in v if second_node in x]
        pos2 = v.index(super_node)
        v[pos1] = v[pos1] + v[pos2]
        e[pos1] = e[pos1] + e[pos2]
        e[pos1] = [x for x in e[pos1] if x not in v[pos1]]
        del v[pos2]
        del e[pos2]
    return len(e[0])

def min_cut(v, e):
    cut = sys.maxsize
    n = len(v)
    for i in range(10*n):
        trial_cut = merge_node(v.copy(), e.copy())
        if trial_cut < cut:
            cut = trial_cut
    return cut

filename = sys.argv[1]
vertices = []
edges = []

lines = open(filename,'r').readlines()
for num in lines:
    num = num.split()
    vertices.append([num[0]])
    edges.append(num[1:])

cut = min_cut(vertices, edges)
print(cut)
