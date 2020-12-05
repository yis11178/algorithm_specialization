import sys
import heapq

# Store the lowest half of numbers so far
# Max heap
# all numbers are negated to behave as min heap
H_low = []
# Store the highest half of numbers so far
# Min heap
H_high = []
# Sore the median of each step
median = []


filename = sys.argv[1]

lines = open(filename,'r').readlines()
for line in lines:
    num = int(line.strip())

    # Add the first two to H_low
    # add the rest according to value
    if len(H_high) == 0 or num < H_high[0]:
        heapq.heappush(H_low, -1*num)
    else:
        heapq.heappush(H_high, num)

    # If one heap has 2 more elements than the other
    # Extract the min/max and push to the other heap
    if len(H_low) - len(H_high) == 2:
        heapq.heappush(H_high, -1*heapq.heappop(H_low))
    elif len(H_high) - len(H_low) == 2:
        heapq.heappush(H_low, -1*heapq.heappop(H_high))

    # Retrieve medion from the heap
    if len(H_low) >= len(H_high):
        median = median + [-1*H_low[0]]
    else:
        median = median + [H_high[0]]

print(sum(median)%10000)