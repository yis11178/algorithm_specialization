import heapq
import sys

def dijkstra(graph, source):
    dist[source] = 0
    heap = []
    for v in graph:
        heapq.heappush(heap, [dist[v], v])
    while heap:
        # Adjacent edges that minimizes A[v] + length(v,w)
        _, u = heapq.heappop(heap)
        for head in graph[u]:
            # Update distance for adjacent edges from source
            alt = dist[u] + graph[u][head]
            if alt < dist[head]:
                dist[head] = alt
                heap = [x for x in heap if x[1]!=head]
                heapq.heappush(heap, [alt, head])
    return None


filename = sys.argv[1]
num = int(sys.argv[2])
# Distance from the source node
# consists of num+1 elements since the vertex numer starts with 1
dist = [1000000 for i in range(num+1)]
# Length of edges
graph = {}

lines = open(filename, 'r').readlines()

# Establish a dictionary of length of edges
for vertex in lines:
    v, edges = vertex.split()[0], vertex.split()[1:]
    graph[int(v)] = {}
    for edge in edges:
        head, dis = edge.split(',')
        graph[int(v)][int(head)] = int(dis)

dijkstra(graph, 1)

print(dist[7], dist[37], dist[59], dist[82], dist[99], dist[115], dist[133], dist[165], dist[188], dist[197])