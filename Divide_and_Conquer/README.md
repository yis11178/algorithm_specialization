# Divide and Conquer

  ## Karatsuba
  Multiplication of `x` and `y`, which are numbers of `n` digits

  Let 

  > x = 10^(n/2)a + b

  > y = 10^(n/2)c + d

  Then

  > x*y =  10^n * ac + 10^(n/2) * (ad + bc) + bd

    1. Calculate a * c
    2. Calculate b * d
    3. Calculate (a + b)(c + d)
    4. Use 3 - 2 - 1
    5. 10^n * 1 + 2 + 10^(n/2) * 4

## Merge Sort


## Strassen's Algorithm


## The Closest pair


## Quick Sort
  ### Overall algorithm
    1. Choose a pivot
    2. Partition the array with pivot
    3. numbers on the left of the pivot is smaller than the pivot,
       numbers on the right of the pivot is larger than the pivot
    4. Recursive call on left partition
    5. Recursive call on right partition
  
  ### Partition the array
  
  If additional memory is allowed: 
  
    array = []
    array += pivot
    for i in array:
      if i < pivot:
        array = i + array // Insert from left
       else:
        array = array + i // Insert from right
   
   If no additional memory is allowed: 
   
    arr: array to be partitioned
    i: boundary between smaller number and larger number among seen numebrs
    j: boundary between seen and unseen numbers
    swap(pivot, arr[0])
    for j in range(len(arr)):
      if arr[k] < pivot:
        swap(arr[k], arr[i])
        i += 1
    swap(pivot, arr[i])
    
  ### Choose the pivot
  
  Worse case senario: 
  `O(n^2)` running time if the first element is chosen as pivot to sort a sorted array. 
  This is the most unbalanced split. 
  
  Best case senario: 
  Median element is chosen as pivot 
  The array is divided into 2 balanced partitions for every recursive call. 
  `O(n*log(n))` running time.
  
  #### Random pivots (Randomization)
  
  1. Choose the pivots with equal probability 
  2. Partition the array
  3. Choose pivots again with each partition 
