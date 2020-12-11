import sys

filename, start, end = sys.argv[1:4]
start = int(start)
end = int(end)

hash_table = {}

# Create a hash table for the array of integers
lines = open(filename,'r').readlines()
for line in lines:
    num = int(line.strip())
    hash_table[num] = None
print("Finish creating hash table!")

# Count of eligible sums
count = 0
# Go through range of numbers
for i in range(start, end+1):
    if i%1000 == 0:
        print("Assessing sum", i)
        print("count so far", count)
    # Iterate through keys in hash table
    for key in hash_table:
        # Search for the compliment number
        # the numbers have to be distinct
        if i-key in hash_table and key*2 != i:
            count += 1
            break

print(count)