# Data Structure

## Heap (Priority Queue)

A container for objects have keys

### Basic Operations

1. Insert: 

    add a new object to the heap
  
    Running time: O(logn)
  
2. Extract min (extract max as well):

    remove an object from the heap with a minimum key value
  
    Running time: O(logn)

3. Heapify:

    Restore heap property
    
    Runing time: O(n)
    
4. Delete (arbitrary one):

    Runing time: O(logn)
  
### Application:

1. HeapSort:

    Using heap to implement SelectionSort algorithm 
    
    Running time: O(logn)
    
    **Selection Algorithm:**
    
    scan through N items, get minimum; scan the rest N-1, get second minimum ...
    
    Runing time: O(N^2)
  

  
2. Event Manager

    **Objects:** event record 
    
    **Keys:** Time event scheduled to occur
    
    **Value:** Event to occur
  
3. Median maintanence:

    **Input:** a sequence of number, one-by-obe
    
    **Output:** at each time step, the median of given number
    
    **Constraint:** O(logi) running time at step i
    
    **Solution:** 2 heaps, H_low supports extract_max, H_high supports extrat_min. 
    
    maintain i/2 smallest number in H_low, largest half in H_high.
  
4. Speeding Dijkstra algorithm

### Implementation: 

  1. Tree
    
  2. Array
  
## Sorted Array -- Static

### Basic Operations

  1. Search
  
  Running time: O(logn)
  
  2. Select
  
  Running time: O(1)
  
  3. Rank (number of keys less than or equal to given value)
  
  Running time: O(logn)
  
## Binary Search Trees -- Dynamic 

  Support all operations of sorted array
  
  Also faster insertion and deletions
  
  Height (longest root-leaf path) can be anywhere between log_2n (perfectly balanced) and n (worst case)
  
### Strucuture

  Exactly one node per key
  
  Each node contains:
    
    Left child pointer
    right child pointer
    parent pointer

### Property

  All left child node is less than the node
  
  All right child node is larger than the node
  
### Basic Operations

  1. Search
  
  Running time: O(logn)
  
  2. Select
  
  Running time: O(n)
  
  3. Rank (number of keys less than or equal to given value)
  
  Running time: O(logn)
  
  4. Insertion:
  
  Running time: o(logn)
  
  5. Deletion:
  
  Running time: o(logn)
  
  **cases**
  
    1. Leaf node: just delete
    
    2. Node has 1 child: delete and connect parent with child
    
    3. Node has 2 children: 
        find predecessor (the largest one that less than node)
        swap node with predecessor
        problem reduced to case2
  
## Hash Table

Maintain a (possibly evolving) set of stuff (transaction, IP address, etc)

### Basic Operations 
a 
Using a 'key', run in constant time

  1. Insert
  
  2. Delete
  
  3. Lookup: check for a particular record
  
### Application

1. De-Duplication

    * Given: a 'stream' of objects
    * Goal: keep track of unique objects
    
2. The 2-SUM problem

    * Given; unsorted array of integers, target sum T
    * Goal: determin whether there is pair that sums to T

### Implementation 

Setup: Universe U (all IP address, all names, all chessboard configuration, etc)

Goal: Want to maintain evolving set S (generally reasonable size) in U 

    array based
    Use hash function to map the value of key to position in array
    
Problem: Collision

    distinct x,y in U, h(x) = h(y)
    
Solution:

* (separate) Chaining
    
    instead of array, use linked list (content of each position makes up of a list)
    Given a key/object, perform Insert/Delete/Lookup in the list in A[h(x)]
    
* Open addressing

    A sequence of hash function h1(x), h2(x), h3(x), ...
    if h1(x) occupied, try h2(x) and so on
    until an open position if found
    
## Bloom Filter

Faster Insert and Lookup

Comparison with Hash table:

    Pros: more space efficient
    Cons: 1. can't store an associated object (only remember what is seen and what is not)
          2. No deletion
          3. small false positive probability

### Application

1. Early spell checkers

2. List of forbidden password

3. Network Routers

### Ingredients

1. array of n bits (only 0/1) (n/|s|=number of bits per object in dataset S)

2. k hash functions

Insert(x):
    for i in range(k):
        set A[hi(x)] = 1 (Regardless of whether bit has been set to 1)
        
Lookup(x): 
    Return True if A[hi(x)] = 1
          
