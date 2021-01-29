import sys
import heapq

filename = sys.argv[1]

lines = open(filename,'r').readlines()
num_nodes = int(lines.pop(0).strip())
# Map that stores the huffman coding of the symbols
# Key: position
# Value: binary code
huffman_code = {i:'' for i in range(num_nodes)}
# Heap that record information during algorithm
# Key: weight (aggregated)
# Value: merged nodes so far
heap = []

for i in range(num_nodes):
    weight = int(lines[i].strip())
    heap += [[weight, [i]]]

heapq.heapify(heap)

while len(heap) > 1:
    w1, node1 = heapq.heappop(heap)
    w2, node2 = heapq.heappop(heap)
    for i in node1:
        huffman_code[i] = '0' + huffman_code[i]
    for i in node2:
        huffman_code[i] = '1' + huffman_code[i]
    heapq.heappush(heap,[w1+w2, node1+node2])

shortest = len(min(huffman_code.values(), key=len))
longest = len(max(huffman_code.values(), key=len))

print('Longest length of codeword: ', longest)
print('Shortest length of codeword: ', shortest)