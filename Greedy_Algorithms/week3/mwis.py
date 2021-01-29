import sys

filename = sys.argv[1]

lines = open(filename,'r').readlines()
num_nodes = int(lines.pop(0).strip())

# Record whether the node is included for the optimal solution
include = [0 for i in range(num_nodes)]
node = []
opt_value = []

for line in lines:
    node += [int(line.strip())]
    opt_value += [int(line.strip())]

# Update the maximum weight indepedent set
# while traversing the list
for i in range(2,num_nodes):
    opt_value[i] = max(opt_value[i-1], opt_value[i] + opt_value[i-2])

pos = num_nodes - 1

# Reconstruction by reversely traverse the list
while pos > 1:
    if opt_value[pos] == opt_value[pos-1]:
        pos -= 1
    else:
        include[pos] = 1
        pos -= 2
if include[2] == 1:
    include[0] = 1
else:
    include[1] = 1
print(include[0], include[1], include[2], include[3], include[16], include[116], include[516], include[996])


