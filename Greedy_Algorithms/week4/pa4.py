import sys

filename = sys.argv[1]
item = []
value = {}

lines = open(filename, 'r').readlines()
total_weight, node_num = lines.pop(0).strip().split(' ')
total_weight = int(total_weight)
node_num = int(node_num)
for line in lines:
    v, w = line.strip().split(' ')
    item += [[int(v), int(w)]]

item = sorted(item, key=lambda x:x[1], reverse=True)

'''
Recursive approach
A large problem can also save space
only saving one column (A[:,i]) of the 2D array A(N * W)
since reconstruction of the solution is not needed.
It can be accelerated by finding the minimum weight of the items.
Weight budget below this value can be discarded (value = 0)
'''
def obtain_values(budget, number):
    # key to the dic that saves value
    key = str(budget) + ' ' + str(number)
    # value and weight of an item
    # The items are sorted in descending order of value from 1~n
    v, w = item[number]
    # If the value is already computed, return it
    if key in value:
        return value[key]
    # If the budget is smaller than the weight, value = 0
    # No need to consider remaining items since they have larger weights
    elif budget < w:
        return 0
    # If this is the last item, just return its value
    elif number == 0:
        value[key] = v
        return value[key]
    # Choose the max between including/not including this item
    else:
        return max(v+obtain_values(budget-w, number-1), 
                obtain_values(budget, number-1))

print('The maximum value is :', obtain_values(total_weight, node_num-1))