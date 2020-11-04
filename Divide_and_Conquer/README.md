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

    1. Choose a pivot
    2. Rearrange the array such that all numbers on the left of the pivot is smaller than the pivot, 
       all numbers on the right of the pivot is larger than the pivot
    3. Do it recursively
    
  If additional memory is allowed: 
  
    ```
    array = []
    array += pivot
    for i in array:
      if i < pivot:
        array = i + array // Insert from left
       else:
        array = array + i // Insert from right
    ```
   
   If no additional memory is allowed: 
   
    ```
    arr: array to be partitioned
    i: boundary between smaller number and larger number among seen numebrs
    j: boundary between seen and unseen numbers
    swap(pivot, arr[0])
    for j in range(len(arr)):
      if arr[k] < pivot:
        swap(arr[k], arr[i])
        i += 1
    swap(pivot, arr[i])
    ```
