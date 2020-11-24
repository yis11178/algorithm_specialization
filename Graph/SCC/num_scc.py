import random
import sys
from collections import deque

'''
Tips:

Recursive method is much slower than iterative method when n gets large

Using list to store explored vertices can be inefficient, consider map

Even using list, avoid "not in/ in" statements

Better way can be used to determine the order. 
'''

def DFS(graph, start, status, backward):
    '''
    graph: dictionary indicating a graph.
    key is the vertex and values is a list of outgoing edges

    start: the start vertex

    status: list that record explored vertex
    '''
    global time
    global stack
    global order
    status.append(start)
    
    if start not in graph:
        return None
    stack += [start]
    popped = []
    while stack:
        v = stack.pop()
        # First node popped out should be the lead
        # The earlier get popped, the larger the finish time
        popped += [v]
        if v not in graph:
            continue
        for next_node in graph[v]:
            if next_node not in status:
                status += [next_node]
                stack.append(next_node)
    '''
    Recursive method:
    for next_node in graph[start]:
        if next_node not in status:
            DFS(graph, next_node, status, backward)
    '''
    if backward == True:
        order = popped + order
    return None


def count_scc(f_graph, b_graph):
    '''
    f_graph: dictionary containing forward directed graph
    b_graph: dictionary containing forward directed graph
    '''
    status = []
    vertice = list(set().union(list(b_graph.keys()), list(f_graph.keys()))) 
    for v in vertice:
        if v not in status:
            DFS(b_graph, v, status, True)
    status = []
    scc_count = []
    before_search = 0
    for vertex in order:
        if vertex not in status:
            DFS(f_graph, vertex, status, False)
            # No of vertices each time DFS explored is the SCC size
            after_search = len(status)
            scc_count.append(after_search-before_search)
            before_search = after_search
    return scc_count


filename = sys.argv[1]
f_graph = {}
b_graph = {}
lines = open(filename,'r').readlines()
print('Creating forward and backward graph')
for num in lines:
    tail, head = num.split()
    if tail not in f_graph:
        f_graph[tail] = []
    f_graph[tail] += [head]
    if head not in b_graph:
        b_graph[head] = []
    b_graph[head] += [tail]

time = 1
stack = deque()
order = []

print('Obtaining number of SCCs')
result = count_scc(f_graph, b_graph)
print(result)
