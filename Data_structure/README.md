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
  
